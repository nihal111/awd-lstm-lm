import os
import torch
import random

from collections import Counter


class Dictionary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = []
        self.counter = Counter()
        self.total = 0

    def add_word(self, word):
        if word not in self.word2idx:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        token_id = self.word2idx[word]
        self.counter[token_id] += 1
        self.total += 1
        return self.word2idx[word]

    def __len__(self):
        return len(self.idx2word)


class Corpus(object):
    def __init__(self, path, vocab_path):
        self.dictionary = Dictionary()
        self.populate_vocab(vocab_path)
        self.train = self.tokenize(os.path.join(path, 'train.txt'))
        self.valid = self.tokenize(os.path.join(path, 'valid.txt'))
        self.test = self.tokenize(os.path.join(path, 'test.txt'))

    def populate_vocab(self, vocab_path):
        with open(vocab_path, 'r') as f:
            content = [line.strip() for line in f.readlines()]

        # Add words to the dictionary
        for word in content:
            self.dictionary.add_word(word)

    def shuffle_training_data(self, path):
        tokens = list(self.train.shape)[0]
        self.train = self.tokenize(os.path.join(path, 'train.txt'),
                                   shuffle=True, tokens=tokens)

    def tokenize(self, path, shuffle=False, tokens=0):
        """Tokenizes a text file."""
        assert os.path.exists(path)

        with open(path, 'r') as f:
            content = f.readlines()

        # Calculate tokens in each file if not done before
        if tokens == 0:
            for line in content:
                words = line.split() + ['<eos>']
                tokens += len(words)

        # Tokenize file content
        ids = torch.LongTensor(tokens)
        token = 0

        if shuffle:
            random.shuffle(content)

        for line in content:
            words = line.split() + ['<eos>']
            for word in words:
                ids[token] = self.dictionary.word2idx[word]
                token += 1

        return ids
