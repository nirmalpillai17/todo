# function to break sentences into multiple 
# lines. A dirty way to implement word wrap!
def break_sentence(sentence, length):
   start = 0
   nspace = 0
   lines = list()

   for end, char in enumerate(sentence):
      if char == " ":
         nspace = end
      if end - start > length:
         line = sentence[start:nspace]
         if not line:
            line = sentence[start:end]
            start = end
            end = end + length
         else:
            start = nspace + 1
         lines.append(line)
   lines.append(sentence[start:])
   return "\n".join(lines)
