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
   <===
   
3.
