source_word="container"
target_word="can"
wc={ch:source_word.count(ch) for ch in set(source_word)}
for ch in target_word:
   if ch in wc and wc.get(ch)>0:
       wc[ch]-=1
   else:
       print("not a kanagroo word")
      break
else:
   print("kangaroo word")
