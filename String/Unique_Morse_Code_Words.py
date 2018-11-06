class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        translate = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        letter_dict = dict(zip(letters,translate))
        words_trans = []
        word_con =str() 
        for word in words:
            for letter in word:
                if letter in letter_dict:
                    word_con = word_con + letter_dict[letter]
            words_trans.append(word_con)
            word_con = str() 
        return len(set(words_trans))           
