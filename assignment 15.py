


#2. Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
#text = "Betty bought a bit of butter, But the butter was so bitter,
#  So she bought some better butter, To make the bitter butter better.
import re
t = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
s=re.findall(r'[Bb][\w]{1,20}',t)
print(s)
#end


#3. Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence
sentence = "A, very very; irregular_sentence"
red=re.sub("[;_:,]"," ",sentence)
print(red)
#end


#4.Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = 'Good advice What I would do differently if I was learning to code today
def show (blue):
    blue=re.sub("http\S+\s"," ",blue)
    blue=re.sub("RT"," ",blue)
    blue=re.sub("cc"," ",blue)
    blue=re.sub("#\S+"," ",blue)
    blue = re.sub("@\S+", " ", blue)
    blue = re.sub("\!", " ", blue)
    blue = re.sub("\:", " ", blue)
    blue=re.sub("\s+"," ",blue)
    return blue
blue = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(show(blue))