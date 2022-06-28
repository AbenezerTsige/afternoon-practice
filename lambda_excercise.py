#Lambda Excercise 1

#Consider the List

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]

#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
#print(prog_lang)
lstasc = prog_lang
lstasc.sort(key=lambda x:x[1])
print("#1")
print(lstasc)

#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
lstdec = prog_lang
lstdec.sort(key=lambda x:len(x[0]), reverse = True)
print("#2")
print(lstdec)

#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
lang_a = prog_lang
lang_a = filter(lambda x: 'a' in x[0], lang_a)
print("#3")
print(list(lang_a))

#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]
lstint = list(filter(lambda x: type(x[1]) == int, prog_lang))
print("#4")
print(lstint)

#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
lowtup = list(map(lambda x: x[0].lower(),  prog_lang)) 
lstcount = list(map(lambda x: len(x[0]),  prog_lang))
lowcnt = list(map(lambda x, y: (x,y), lowtup, lstcount))
print("#5")
print(lowcnt)


#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')
print("#6")
prog = tuple(map(lambda x: (x[0]), prog_lang))
vers = tuple(map(lambda y: (y[1]), prog_lang))
print(prog)
print(vers)
prog_tup = prog + vers 
print(prog_tup)
