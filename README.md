# markov-text

Markov chain text generator, implemented in python. Takes in a corpus to build the engine to generate the text chains, and then generates a chain until completion (or until an arbitrary length is reached).
Currently set up to work with a twitter archive.

### to-do
 - input handling for a corpus in the form a single txt file
 - maybe use the twitter api to pull recent tweets from any given twitter user, and use that to generate text (as opposed to having to require access to a user's twitter archive)