# Password Generator

A public algorithm to generate passwords so that you don't need to store them anywhere, thus you can't lose them, and nobody can steal them from you.

Inputs:
 - master password: the only password you need to remember
 - user: the user name for which you want to generate the password
 - website/service/host: the domain name of the website (e.g. www.gmail.com), or the name of the service (e.g. gmail), or the name of the host you want to register in with the user and the generated password
 - year: the year for which you want to use the password for, in YYYY format (e.g. 2023), as you should change your passwords every year

The output is the new password in the following format: word1-word2-word3-word4, where each word is generated (not actual real words). Every word starts with an uppercase letter, and word4 is a number.
