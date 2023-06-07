# Werken met tekst binnen linux


## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
Wederom chatGPT gebruikt. Ik zal i.c. hieronder het antwoord van chatGPT plaatsen waar ik mee gewerkt heb.  

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

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
