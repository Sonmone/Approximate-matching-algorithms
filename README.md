# Approximate matching algorithm
Introduction
-------------
  
The code is based on Python3.5. To run this project, the current computer needs to install Python3.5 or higher Python Version.<br/>

There are three .py programs in the root directory: ged.py contains the method of global edit distance, ns.py contains the method of neighbourhood search, ngram.py contains the method of n-gram distance.<br/>
  
Compilation
-------------
  
Run three .py programs in IDLE (windows) or in command directly.<br/>
  
Files
-------------
  
In the root directory, ged.py, ns.py, ngram.py are three executable scripts; data file includes misspelled.txt, correct.txt and dictionary.txt; Results file includes the output of every method.<br/>
  
Output
-------------
  
The output of each method is stored in the Result file, and gedResult is the output of global edit distance method, nsResult is the output of neighbourhood search method, 2-gramRsult is the output of 2-gram distance method, 3-gramResult is the output of 3-gram distance method.<br/>

In each result file, the first part is the output of every prediction, and the format is as follows:<br/>

Misspelled Word: (represents current misspelled word)<br/>
Correct Word: (represents current correct word)<br/>
Predicted Word: [] (contains all predicted words)<br/>
Score: x of y (x is 0 or 1 representing whether predict correctly; y is the number of all predicted words)<br/>
******************************************** (separator)<br/>
In the end of each file, Precision and Recall are calculated of this method.<br/>
