# Create your Dictionary
print("Hi, This your dictionary.Search for the hard texts and get their meanings.")

dictionary = {"abnegation":{"def":"Renouncing a belief or doctrine",
                            "ex":"I believe in the abnegation of political power"},
              "disparate":{"def":"of a distinct kind","ex":"They inhabit disparate worlds of thought."},
              "denigrate":{"def":"belittle someone","ex":"There are many doom and gloom merchants who denigrate their own country."},
              "construe":{"def":"interpret or assign meaning","ex":" His words could hardly be construed as an apology."}}
print("Enter the the work you want to search for: ")
query_word = input()
search_value = query_word.lower()

print("The meaning of",query_word,"is:",dictionary[search_value]["def"],". For Example:",dictionary[search_value]["ex"])