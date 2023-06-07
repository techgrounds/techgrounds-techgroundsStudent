# Werken met tekst binnen linux


## Key-terms
**Pipe**  
Dit is het symbool om de output van een command de input te maken van een andere command. 

## Opdracht 
1. Use the echo command and output redirection to write a new sentence into your text file using the command line. The new sentence should contain the word ‘techgrounds’.  
2. *Use a command to write the contents of your text file to the terminal. Make use of a command to filter the output so that only the sentence containing ‘techgrounds’ appears.*


## Gebruikte bronnen
Wederom chatGPT gebruikt. Ik zal i.c. hieronder de antwoorden van chatGPT plaatsen waar ik mee gewerkt heb.  

In Ubuntu, pipes are a powerful feature of the command-line interface that allows you to connect the output of one command as the input to another command. This enables you to perform complex operations by combining simple commands. The syntax for using a pipe is the vertical bar symbol "|".

Here's an example of how to use a pipe in Ubuntu:

1. Open a terminal by pressing Ctrl+Alt+T or by searching for "Terminal" in the applications.
2. Type a command and use the pipe symbol "|" followed by another command.

For instance, let's say you want to list all the files in a directory and then search for a specific file within the list. You can use the "ls" command with the pipe to pass its output to the "grep" command for filtering. Here's the example:

```bash
ls | grep myfile.txt
```

In this example, the "ls" command lists all the files in the current directory, and the output is passed through the pipe to the "grep" command, which filters the results and displays only the lines containing "myfile.txt".

You can use pipes with various commands and combine them to achieve more complex operations. Some common use cases include sorting, filtering, searching, and data processing.

Note that pipes work by passing the standard output (stdout) of the preceding command as the standard input (stdin) of the following command. Therefore, not all commands are compatible with pipes, as they may require interactive input or rely on other forms of data transmission.

I hope this helps you understand how to use pipes in Ubuntu! Let me know if you have any further questions.

-------

The pipe command (`|`) is used to redirect the output of one command as the input of another command. However, it does not save the output directly to a file. To save the output of the `echo` command to a text file using the pipe command, you can use the `tee` command. Here's an example:

```bash
echo "Hello, World!" | tee newfile.txt
```

In this example, the `echo` command outputs the text "Hello, World!" and the pipe (`|`) redirects that output to the `tee` command. The `tee` command takes the input and saves it to a file specified as an argument (`newfile.txt` in this case). The `tee` command also displays the input on the terminal.

After executing the command, the text "Hello, World!" will be saved in the `newfile.txt` file. If the file doesn't exist, it will be created. If the file already exists, the previous content will be overwritten.

If you want to append the output to an existing file rather than overwriting it, you can use the `-a` option with the `tee` command:

```bash
echo "Hello, World!" | tee -a existingfile.txt
```

This command will append the output to the `existingfile.txt` instead of overwriting it.

I hope this helps! Let me know if you have any further questions.



## Ervaren problemen


## Resultaat
1. Het bestand beproeving.txt heeft gediend om deze opdracht te vervullen. Zie [hier](/01_Linux_3/1.toevoeging.PNG) om te zien met welke commands ik de tekst daadwerkelijk heb toegevoegd. [Vergelijk](./1.1.Snip.PNG) daarnaast ook om daadwerkelijk te zien dat het gelukt is tekst bij te sluiten. 
2. 