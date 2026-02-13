import numpy as np
import torch

# class to store a language
class Language:
    # initialize the language, as standard we have start of sentence (SOS), end of sentence (EOS) and a padding to equalize sentence lengths (PAD)
    def __init__(self, name, codon_len):
        self.name = name
        self.word2index = {}
        self.index2word = {}
        self.n_words = 0
        self.codon_length = codon_len


    # function to split sentence in blocks of a given codon_length
    def splitSentence(self, sentence):
        return [sentence[i:i+self.codon_length] for i in range(0,len(sentence),self.codon_length) if len(sentence[i:i+self.codon_length])==self.codon_length]


    # function to add sentence to language (add all new words in the sentence to our language)
    def learnWords(self, sentence):
        sentence_split = self.splitSentence(sentence)
        for word in sentence_split:
            if word not in self.word2index:
                self.word2index[word] = self.n_words
                self.index2word[self.n_words] = word
                self.n_words += 1


    # function to count the word frequencies in a sentence
    def encode(self, sentence):
        sentence_split = self.splitSentence(sentence)
    
        ############################
        ### create a tensor having the number of available words as length, fill with with zeros
        codon_freqs = torch.zeros(self.n_words)
        ############################

        # count frequencies of every word in the sentence
        word_counts = np.unique(sentence_split, return_counts = True)
        for i in range(len(word_counts[0])):
            codon_freqs[self.word2index[word_counts[0][i]]] = word_counts[1][i]
        codon_freqs /= len(sentence_split)

        return codon_freqs


    # return a sample of frequencies for all words in a language
    # here we're matching the codon frequencies to the sequence length of the provided sequence
    def sample_sentence(self, sentence):
        # create a tensor having the number of available words as length, fill with with zeros
        codon_freqs = torch.zeros(self.n_words)

        # sample nr of codons in sequence based on actual data
        # generate random sequence of codons given the current sequence length
        nr_codons = round(len(sentence)/self.codon_length)
        sampled_codons = list(np.random.randint(low=0, high=self.n_words, size = nr_codons, dtype=int))

        # count frequencies of every codon
        word_counts = np.unique(sampled_codons, return_counts = True)
        for i in range(len(word_counts[0])):
            codon_freqs[word_counts[0][i]] = word_counts[1][i]
        codon_freqs /= nr_codons

        return codon_freqs

    
    # here we define a function for encoding an entire dataset sequences
    def encode_dataset(self, dataset):
        # encode positives
        encoded_positives = [{'sample':self.encode(sentence),'label':torch.Tensor([1])} for sentence in dataset]

        # sample negatives following the sequence length distribution of positives
        encoded_negatives = [{'sample':self.sample_sentence(sentence),'label':torch.Tensor([0])} for sentence in dataset]

        # merge datasets and randomly mix positives and negatives
        dataset_encoded = encoded_positives + encoded_negatives
        random.shuffle(dataset_encoded)
        
        return dataset_encoded
        

    # here we define a function for encoding an entire dataset sequences
    def encode_positives(self, dataset):
        # encode positives
        encoded_positives = [{'sequence':sentence,'frequencies':self.encode(sentence),'label':torch.Tensor([1])} for sentence in dataset]
        return encoded_positives


    # here we define a function for encoding an entire dataset sequences
    def encode_negatives(self, dataset):
        # sample negatives following the sequence length distribution of positives
        encoded_negatives = [{'sequence':sentence,'frequencies':self.sample_sentence(sentence),'label':torch.Tensor([0])} for sentence in dataset]
        return encoded_negatives

