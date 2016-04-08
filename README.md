# markov-text

The goal of this project is to use markov chains to predict text based on a corpus. I think it might be fun to mess around with markov chains and it should serve as a relatively interesting project. 

This is preliminary planning. Work on this project started as a result of a 30-day git commit challenge, so the goal is to make a little progress every day (even if its as little as designing and updating this ReadME). This ReadME will serve as a sounding board for the current design as I work on this side project. 
### to-do
- design class hierarchy for the project
   - class to represent  (word1, word2, ..., wordn) and all the words they lead to (maybe use a member to hold all the result words, as well as probabilities)
   - class to run the actual chaining to generate sentences
- handle input: processing, creating the map of probabilities
