Redsheep's Python note.
======

1. string and tuple are immutable. list is mutable.
   str = "hfjiang"
   str[0] = 'm' # error
   
   tuple = ("hfjiang", 100)
   tuple[0] = "mmyang" # error
   
   list1 = [1,2,3]
   list1[0] = 0 # [0,2,3]
   
   str1 = "banana"
   str2 = "banana"
   str1 is str2 # True, refer to the same object (memory address)
   
   list1 = [1,2,3]
   list2 = [1,2,3]
   list1 == list2 # True
   list1 is list2 # False, refer to the different object (memory address)

   list3 = list1 # Aliasing, refer to same object
   list3 is list1 # True
   list3[0] = 4 # list1 = [4,2,3]
   
   list1 = [1,2,3]
   list4 = list1[:] # cloning list, refer to different object
   list4[0] = 5 # list1 = [1,2,3]
   
2. Pure functions and modifiers
   The following sayings are very important, digested from thinkcspy3 pg. 155.
   ===>
   """
   Functions which take lists as arguments and change them during execution are called modifiers
   and the changes they make are called side effects.
   
   A pure function does not produce side effects. It communicates with the calling program only
   through parameters, which it does not modify, and a return value. Here is double_stuff written
   as a pure function:
   """
   def double_stuff(a_list):
        """ Return a new list which contains
            doubles of a the elements in a_list.
        """
        new_list = []
        for value in a_list:
            new_elem = 2 * value
            new_list.append(new_elem)
            
        return new_list
    The version of double_stuff does not change its arguments:
    things = [2,5,9]
    xs = double_stuff(things)
    things # [2,5,9]
    xs # [4, 10, 18]
    
    An early rule we saw for assignment said "first evaluate the right hand side, then assign the
    resulting value to the variable". So it is quite safe to assign the function result to the same
    variable that was passed to the function:
    things = [2,5,9]
    things = double_stuff(things)
    things # [4, 10, 18]
    
    Anything that can be done with modifiers can also be done with pure functions. In fact, some
    programming languages only allow pure functions. There is some evidence that programs that use pure
    functions are faster to develop and less error-prone than programs that use modifiers. Nevertheless, 
    modifieres are convenient at times, and in some cases, functional programs are less efficient.
    
    In general, we recommend that you write pure functions whenever it is reasonable to do so and
    resort to modifiers only if there is a compelling advantage. This approach might be called a 
    functional programming style.
    
    The important pattern for pure function:
    <begin>
    initialize a result variable to be an empty list
    loop
        create a new element
        append it to result
    return the result
    <end>
    
   <===
   
3. string split and join
   str = "hfjiang mmyang"
   names = str.split()
   glue = ";"
   glue.join(names)# "hfjiang;mmyang"

4. How are namespaces, files and modules related?
5. Attributes and the dot operator
    Variables defined inside a module are called attributes of the modules. We've seen that objects
    have atrributes too: for example, most objects have a __doc__ attribute, some functions have a __annotations__ attribute.
    Attributes are accessed using the dot operator(.).
6. How to deal with file open fail?
    
    Use try .. except like this:
        try:
            f = open(filename, 'r')
        except:
            print ("can not open file named", filename)
            
    But if we want to check if a file exists, we can use os.path module:
    import os
    # the preferred way to check if a file exists
    if os.path.isfile("c:/temp/yourfile.txt"):
        ...
    
7. The power of translate method of string.
    def text_to_words(the_text):
        """ Return a list of words with all punctuation removed,
            and all in lowercase.
        """
        my_substitution = the_text.maketrans(
        # if you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~",
        # Replace them by these (must have equal length with first str)
        "abcdefghijklmnopqrstuvwxyz                                        ")
        
        #Translate the text now.
        cleaned_text = the_text.translate(my_substitution)
        wds = cleaned_text.split()
        return wds
    print (text_to_words('"Well, I never!", said Alice.') == ["well", "i", "never","said", "alice"])
8.  How to represent a null object? Just use 'None'.
    pre_ele = None
    for e in ele_list:
        if e != pre_ele:
            do_sth
            pre_ele = e
        else:
            do_others
9. set the default parameters for function.
    def func(x=0, y=1):
        return (x,y)
    print(func()) # (0,1)
    print(func(5,6)) # (5,6)
10. The sameness  of Class objects
    Shallow equality: compares only the references, not the contents of the objects
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p1 is p2 # False
    p3 = p1
    p1 is p3 # True
    
    Deep equality: compre the contents of the objects.
    def same_coord(p1, p2):
        return (p1.x == p2.x) and (p1.y == p2.y)
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    same_coord(p1,p2) # True
    
    Beware! By default "==" on (user defined) Class objects does a shallow equality test.
    p1 = Point(3, 4)
    p2 = Point(3, 4)
    (p1 == p2) # False
    
    But, By default "==" does a deep equality test on lists.
    a = [1,2]
    b = [1,2]
    a == b  # True
   
11. The shallow copy and deep copy of Class objects
    
    Shallow copy can copy simple object like Point.
    import copy
    p1 = Point(3, 4)
    p2 = copy.copy(p1)
    p1 is p2 # False, different object
    same_coord(p1,p2) # True, contents same
    
    But, for complex object like Rectangle, which contains a reference to a Point, 'copy' 
    doesn't do quite the right thing. It copyies the reference to the Point object. So both
    the old rec and new one refer to a single Point.
    
    
    Rectangle(corner, height, width) # corner is a Point(x,y) object
    rec1 = Rectangle(Point(1, 2),10,8)
    rec2 = copy.copy(rec1)
    rec1.corner is rec2.corner # True, refer to a single Point.
    
    rec3 = copy.deepcopy(rec1) # deepcopy can do the right thing!!
    rec1.corner is rec3.corner # False, refer to diff Points.
    
    
12. Dict
    (0) string, list, tuple are sequence types, which use integers as indices to access
        values they contained within them. Dict is not sequence type, so we can't 
        index or slice a dictionary.
    (1) Keys can be any immutable type, values can be any type.
    (2) The empty dictionary is denoted {}
        mydict = {}
    (3) The order of the pairs(key:value) is unpredictable. Since Python uses complex
        algorithms, designed for very fast access, to determine where the key:value pairs 
        are stored in a dictionary.
    (4) Dict vs. Tuple.
        You might wonder why we use dictionaries at all when the same concept of mapping a key
        to a value could be implemented using a list of tuples. The reason is dictionaries are 
        very fast, implemented using a technique called "hasing", which allow us to access a value
        very quickly. By contrast, the list of tuples implementation is slow. If we wanted to
        find a value associated with a key, we would have to iterate over every tuple, checking the 0th
        element. What if the key wasn't even in the list? We would have to get to the end of it to find out!
    (5) Aliasing and copying.
        As in the case of lists, because dictionaries are mutablem we need to be aware of aliasing.
        Whenever two variables refer to the same object, changes to one affect the other.
        
        If we want to modify a dictionary and keep a copy of the original, use the 'copy' method. 
        op = {"up": down", "right":"wrong"}
        alias = op
        copy = op.copy() # shallow copy
        copy["right"] = "left"
        op["right"] # "wrong"
        alias["right"] = "bad"
        op["right"] # "bad"
        
        But, how to do deep copy? Dict has no deepcopy method (for now??), we can use 
        the deepcopy of copy module.
        import copy
        mydic = {"hfjiang":[2,3,4,5], "mmyang":["girl","boss"]}
        dcopy = copy.deepcopy(mydic)
        dcopy["mmyang"][0] = "boy"
        print(mydic["mmyang"]) # ['girl', 'boss']
        scopy = mydic.copy()
        scopy["mmyang"][0] = "boy or girl"
        print(mydic["mmyang"])#['boy or girl', 'boss']
        
        
    (6) Dict can represent sparse matrix efficiently.
        (I have seen the more sophisticated version of matrix implemention 
        in Coursera "Coding the Matrix")
        The list of lists representation:
            matrix = [[0,0,1,0,0],
                      [0,1,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,8]
                    ]
        The dict representation:
            matrix = {(0,2):1, (1,1):1, (3,3):8}
        There is one problem. If we specify an elementary that is zero, we get an error, because there 
        is no entry in the dictionary with that key:
            matrix[(1,3)] # KeyError: (1,3)
        The get method solves this problem:
            matrix.get((0,2), 0) # return 1
            matrix.get((1,3), 0) # return 0
        The first argument is the key; the second argument is the value 'get' should return if the key
        is not in the dictionary.
13. The comma in print
    for i in range(0,5):
        print(i)
    #output
    0
    1
    2
    3
    4
    for i in range(0,5):
        print(i),
    #output
    0 1 2 3 4
    
    NB: It seems that Python3 doesn't work like this!
14. 