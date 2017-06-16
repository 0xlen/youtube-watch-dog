# -*- coding: utf-8 -*-

import codecs
import operator

class ngram:

    def __init__(self):

        self.words_freq = {}
        self.max_count = 0

    def ishan(self, text):
        return all(u'\u4e00' <= char <= u'\u9fff' for char in text)

    def executeNgram(self, text, n):
        words=[]

        for w in range(len(text)-n):
            extract = text[w:w+n].strip()
            if len(extract) == n:
                words.append(extract)

        for word in words:
            if word not in self.words_freq and self.ishan(word):
                self.words_freq[word] = 1
            elif word in self.words_freq and self.ishan(word):
                self.words_freq[word] = self.words_freq[word] + 1


    def regress(self):
        j = 0
        while j < len(self.words_freq):

            # Update max value
            self.max_count = max(self.words_freq[j][1], self.max_count)

            k = 0
            while k < len(self.words_freq):
                if j == k:
                    k = k + 1
                    continue

                if j >= len(self.words_freq) or k >= len(self.words_freq): break

                word = self.words_freq[j]
                compare_word = self.words_freq[k]

                # find duplicate word and maximize the word set
                if compare_word[0] in word[0] and word[1] >= compare_word[1] and len(word[0]) > len(compare_word[0]):
                    # remove compare_word
                    del self.words_freq[k]
                else:
                    k = k + 1

            j = j + 1

    def process(self, text):
        text_new = []
        for line in text:
            # line = codecs.decode(line, "utf-8")
            text_new.append(line)

        min_count = min(map(len, text_new))

        for line in text_new:
            for count in range(2, len(line)):
                self.executeNgram(line, count)

        self.words_freq = sorted(self.words_freq.iteritems(),key=operator.itemgetter(1),reverse=True)

        self.regress()

        return self.words_freq

    def getMax(self):
        return self.max_count
