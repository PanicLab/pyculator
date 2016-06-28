# Encoding: utf-8
# Language: russian

from math import sqrt
from decimal import Decimal

from widgets import *

class Data:

    class Encapsulator:
    
        def __init__(self, value=""):
        
            self._arg = value
            
            
        def __get__(self, instance, cls):

            return self._arg


        def __set__(self, instance, _some_arg):

            self._arg = _some_arg
            
    
    arg1 = Encapsulator()
    arg2 = Encapsulator()
    input_arg = Encapsulator()
    memory = Encapsulator(0)
    math_operation = Encapsulator()
    input_is_float = Encapsulator(False)
    on_display = Encapsulator("0")
    mem_displayed = Encapsulator()



class Analyzer:
    
    find_no_args_no_input_arg = False
    find_no_args_no_mathop_just_input_arg = False
    find_arg1_only = False
    find_arg1_and_mathop = False
    find_arg1_mathop_and_input_arg = False

    
    @staticmethod
    def detect_input_stage():
        
        Analyzer.find_no_args_no_input_arg = False
        Analyzer.find_no_args_no_mathop_just_input_arg = False
        Analyzer.find_arg1_only = False
        Analyzer.find_arg1_and_mathop = False
        Analyzer.find_arg1_mathop_and_input_arg = False
    
        if (Data.arg1 !="" and Data.math_operation !="" 
                           and Data.input_arg !=""):
                           
            Analyzer.find_arg1_mathop_and_input_arg = True

            
        if (Data.arg1 !="" and Data.math_operation !=""
                           and Data.input_arg ==""):
                           
            Analyzer.find_arg1_and_mathop = True
 
 
        if (Data.arg1 !="" and Data.math_operation ==""
                           and Data.input_arg ==""):
                           
            Analyzer.find_arg1_only = True
 
 
        if (Data.arg1 == "" and Data.math_operation == ""
                            and Data.arg2 == ""
                            and Data.input_arg != ""):
                            
            Analyzer.find_no_args_no_mathop_just_input_arg = True
   
   
        if (Data.arg1 == "" and Data.arg2 == ""
                            and Data.input_arg == ""):
                            
            Analyzer.find_no_args_no_input_arg = True


    
    @staticmethod
    def setup_input_arg_float_status():
    
        if "." in Data.input_arg:
        
            Data.input_is_float = True
            
                
        else:
        
            Data.input_is_float = False        

            
    
    @staticmethod
    def remove_trailing_symbols_if_necessary():
    
        if not Data.input_is_float:
        
            return
            
        while Data.input_arg.endswith("0"):
        
            Data.input_arg = Data.input_arg[:-1]

        
        if Data.input_arg.endswith("."):
        
            Data.input_arg = Data.input_arg[:-1]
            
        
        Analyzer.setup_input_arg_float_status()    



class Calculator:

    def add_spaces(function):

        def decorator():

            if "e" in Data.input_arg or "E" in Data.input_arg:
            
                function()
                return
            
            Analyzer.setup_input_arg_float_status()
            if Data.input_is_float:
                integer_part, fraction_part = Data.input_arg.split(".")

            else:
                integer_part = Data.input_arg
                fraction_part = ""

                
            sign = ""
            if "-" in integer_part:
            
                sign = "-"
                integer_part = integer_part[1:]
            
            
            number_of_spaces = len(integer_part)//3
            if number_of_spaces < 1: 
                
                function()
                return 

            decorated = ""
            for x in range(len(integer_part)-1, -1, -1):

                if (len(integer_part)-1-x)%3:
                    decorated += integer_part[x]

                else:
                    decorated = " ".join((decorated, integer_part[x]))


            decorated = list(decorated)
            decorated.reverse()
            integer_part = ""
            for x in decorated:
                integer_part += x           
            integer_part = sign + integer_part.rstrip()

            if Data.input_is_float:
                Data.on_display = ".".join((integer_part, fraction_part))
            
            else:
                Data.on_display = integer_part

                
        return decorator



    @staticmethod
    @add_spaces
    def update_displayed_data():
    
        Data.on_display = Data.input_arg
        

        
    @staticmethod
    def set_new_arg():
    # Получаем аргумент для последующего арифм. действия.

        Calculator.convert_input_arg_to_digit()
        
        if Data.arg1 == "":             # Eсли аrg1 не существует, то...
            
            Data.arg1 = Data.input_arg    # ...то значение получает он,...

            
        else:                           # если arg1 уже существует, то...
              
            Data.arg2 = Data.input_arg    # то значение получает arg2
        
        Calculator.convert_input_arg_to_str()

        

    @staticmethod    
    def convert_input_arg_to_digit():
    
        Data.input_arg = Decimal(Data.input_arg)    
   
   
  
    @staticmethod
    def convert_input_arg_to_str():
    
        Data.input_arg = str(Data.input_arg)
    


    @staticmethod
    def reset_data_after_calculation():

        Data.arg1 = ""
        Data.arg2 = ""
        Calculator.set_new_arg()
        Data.input_arg = ""
        Data.math_operation = ""
        Data.input_is_float = False
        


    @staticmethod
    def make_ordinary_calculation():   # "+", "-", "*", "/", "xy", "%"
    
        if Data.math_operation == "%":
        
            Data.input_arg = Data.arg1 / 100 * Data.arg2
                    
        else:
        
            try:
            
                exec("Data.input_arg = Data.arg1 " + Data.math_operation + " Data.arg2")
                
            except ZeroDivisionError:
            
                Data.input_arg = "0"
                
        Calculator.convert_input_arg_to_str()
        Analyzer.setup_input_arg_float_status()

                 

    @staticmethod
    def make_not_ordinary_calculation(_some_arg, symbol):
    
        def make_sqrt_calculation(_some_arg):
    
            try:
                Data.input_arg = sqrt(_some_arg)

            except ValueError:
                Data.input_arg = "0"
            
            
        def make_1divx_calculation(_some_arg):
    
            try:
            
                Data.input_arg = 1/_some_arg
                
            except ZeroDivisionError:
            
                Data.input_arg = "0"
    
    
        if symbol == "sqrt":
            make_sqrt_calculation(_some_arg)
        
        elif symbol == "1/x":
            make_1divx_calculation(_some_arg)
        
        Data.input_arg = str(Data.input_arg)
        Analyzer.setup_input_arg_float_status()



    @staticmethod
    def set_math_operation(symbol):
    
        Data.math_operation = symbol
        
    
    
    def some_special_cases(function):
    
        def special_cases_decorator(symbol):
        
            if symbol == "00" and Analyzer.find_no_args_no_input_arg:
                Data.input_arg = "0"
                return

            if (symbol == "00" and Analyzer.find_no_args_no_mathop_just_input_arg
                               and Data.input_arg == "0"):

                return
            
            if symbol == "00" and Analyzer.find_arg1_only:
                Data.arg1 = ""
                Data.input_arg = "0"
                return

            if symbol == "00" and Analyzer.find_arg1_and_mathop:
                Data.input_arg = "0"
                return

            if (symbol == "00" and Analyzer.find_arg1_mathop_and_input_arg 
                               and Data.input_arg == "0"):

                return

            if (symbol == "0" and Analyzer.find_no_args_no_mathop_just_input_arg
                              and Data.input_arg == "0"):

                return

            if symbol.isdigit() and Data.input_arg == "0":
        
                Data.input_arg = ""
        
            function(symbol)

            
        return special_cases_decorator
        
                
    
    @staticmethod
    @some_special_cases
    def update_input_arg(symbol):

        Data.input_arg += symbol



class ProcessingEvent:
 
    def use_no_args_no_input_arg_stage_behavior(self, symbol): pass
    def use_input_arg_only_stage_behavior(self, symbol): pass    
    def use_arg1_only_stage_behavior(self, symbol): pass
    def use_arg1_and_mathop_stage_behavior(self, symbol): pass
    def use_arg1_mathop_and_input_arg_stage_behavior(self, symbol): pass
           
    def use_original_logic(self, symbol): pass
    
    @staticmethod
    def output_to_screen():
    
        mainDisplay.set_property("text", Data.on_display)
        memoryDisplay.set_property("text", Data.mem_displayed)


    def __call__(self, widget, symbol):

        Analyzer.detect_input_stage()

        if Analyzer.find_no_args_no_input_arg:
            self.use_no_args_no_input_arg_stage_behavior(symbol)
        
        if Analyzer.find_no_args_no_mathop_just_input_arg:
            self.use_input_arg_only_stage_behavior(symbol)
        
        if Analyzer.find_arg1_only:
            self.use_arg1_only_stage_behavior(symbol)
            
        if Analyzer.find_arg1_and_mathop:
            self.use_arg1_and_mathop_stage_behavior(symbol)
            
        if Analyzer.find_arg1_mathop_and_input_arg:
            self.use_arg1_mathop_and_input_arg_stage_behavior(symbol)

        self.use_original_logic(symbol)
        self.output_to_screen()

       

class Processing_C(ProcessingEvent):

    def use_original_logic(self, symbol):
    
        Data.arg1 = ""
        Data.arg2 = ""
        Data.input_arg = ""
        Data.math_operation = ""
        Data.input_is_float = False
        Data.on_display = "0"


        
class Processing_Mc(ProcessingEvent):

    def use_original_logic(self, symbol):
    
        Data.memory = 0
        Data.mem_displayed = ""
    
    
    
class Processing_MinusPlus(ProcessingEvent):

    def use_original_logic(self, symbol):
    
        if not Data.input_arg or Data.input_arg == "0":
            return

        if not Data.input_arg.startswith ("-"):
            Data.input_arg = Data.input_arg.replace(Data.input_arg, "-" + Data.input_arg)

        else:
            Data.input_arg = Data.input_arg.lstrip("-")
                
        Calculator.update_displayed_data()
        
        
        
class Processing_Comma(ProcessingEvent):

    def use_no_args_no_input_arg_stage_behavior(self, symbol):
    
        Data.input_arg = "0"
        
    
    def use_arg1_only_stage_behavior(self, symbol):
    
        Data.arg1 = ""
        Data.input_arg = "0"
        
        
    def use_arg1_and_mathop_stage_behavior(self, symbol):
          
        Data.input_arg = "0"
        
    
    def use_original_logic(self, symbol):
    
        if not Data.input_is_float:
            Calculator.update_input_arg(symbol)
            Data.input_is_float = True
        
        Calculator.update_displayed_data()
        


class Processing_Digit(ProcessingEvent):

    def use_arg1_only_stage_behavior(self, symbol):
    
        Data.arg1 = ""
        
        
    def use_original_logic(self,symbol):
    
        Calculator.update_input_arg(symbol)
        Calculator.update_displayed_data()
        
        
        
class Processing_Mr(Processing_Digit):

    def use_original_logic(self, symbol):
    
        Data.input_arg = str(Data.memory)
        Calculator.update_displayed_data()


        
class Processing_Bs(ProcessingEvent):

    def use_input_arg_only_stage_behavior(self, symbol):
    
        Data.input_arg = Data.input_arg[:-1]
        if Data.input_arg == "" or Data.input_arg == "-":
            Data.input_arg = "0"
                
        Calculator.update_displayed_data()
        Data.input_arg == ""

    def use_arg1_mathop_and_input_arg_stage_behavior(self, symbol):
    
        self.use_input_arg_only_stage_behavior(symbol)
        
        

class Processing_Ms(ProcessingEvent):

    def use_no_args_no_input_arg_stage_behavior(self, symbol):
    
        Data.memory = 0
        
        
    def use_input_arg_only_stage_behavior(self, symbol):
    
        Calculator.convert_input_arg_to_digit()
        Data.memory = Data.input_arg
        Calculator.convert_input_arg_to_str()
        
    
    def use_arg1_only_stage_behavior(self, symbol):
    
        Data.memory = Data.arg1
        
    
    def use_arg1_and_mathop_stage_behavior(self, symbol):
    
        self.use_arg1_only_stage_behavior(symbol)
        
        
    def use_arg1_mathop_and_input_arg_stage_behavior(self, symbol):
    
        self.use_input_arg_only_stage_behavior(symbol)
        
    
    def use_original_logic(self, symbol):
    
        Data.mem_displayed = " M"
        
        

class Processing_Mplus(Processing_Ms):

    def use_no_args_no_input_arg_stage_behavior(self, symbol):
    
        super().use_no_args_no_input_arg_stage_behavior(symbol)
        Data.input_arg = "0"
        Calculator.update_displayed_data()
        Calculator.reset_data_after_calculation()
        
        
    def use_input_arg_only_stage_behavior(self, symbol):
    
        Calculator.convert_input_arg_to_digit()
        Data.memory = Data.memory + Data.input_arg
        Calculator.convert_input_arg_to_str()
        
        
    def use_arg1_only_stage_behavior(self, symbol):
    
        Data.memory = Data.memory + Data.arg1
        
        
        
class Processing_Equal(ProcessingEvent):

    def use_arg1_mathop_and_input_arg_stage_behavior(self, symbol):
    
        Calculator.set_new_arg()
        Calculator.make_ordinary_calculation()
        Analyzer.remove_trailing_symbols_if_necessary()
        Calculator.update_displayed_data()
        Calculator.reset_data_after_calculation()
        
        
    
class Processing_OrdinaryOperation(Processing_Equal):

    def use_no_args_no_input_arg_stage_behavior(self, symbol):
    
        Data.input_arg = "0"
        Calculator.set_new_arg()
        Calculator.update_displayed_data()
        Calculator.reset_data_after_calculation()
        
        
    def use_input_arg_only_stage_behavior(self, symbol):
    
        Analyzer.remove_trailing_symbols_if_necessary()
        Calculator.set_new_arg()
        Calculator.update_displayed_data()
        Data.input_arg = ""
        Data.input_is_float = False
        
    
    def use_original_logic(self, symbol):
    
        Calculator.set_math_operation(symbol)
        
        
        
class Processing_NotOrdinaryOperation(Processing_Equal):

    def use_arg1_mathop_and_input_arg_stage_behavior(self, symbol):
    
        Calculator.set_new_arg()
        Calculator.make_not_ordinary_calculation(Data.arg2, symbol)
        super().use_arg1_mathop_and_input_arg_stage_behavior(symbol)
        
    
    def use_arg1_and_mathop_stage_behavior(self, symbol):
    
        Calculator.make_not_ordinary_calculation(Data.arg1, symbol)
        Analyzer.remove_trailing_symbols_if_necessary()
        Calculator.update_displayed_data()
        Calculator.reset_data_after_calculation()
        
        
    def use_arg1_only_stage_behavior(self, symbol):
    
        self.use_arg1_and_mathop_stage_behavior(symbol)
        
    
    def use_input_arg_only_stage_behavior(self, symbol):
    
        Calculator.set_new_arg()
        self.use_arg1_and_mathop_stage_behavior(symbol)
    
   
   
button_c.connect("clicked", Processing_C(), "c")
button_bs.connect("clicked", Processing_Bs(), "bs")
button_plus.connect("clicked", Processing_OrdinaryOperation(), "+")
button_mc.connect("clicked", Processing_Mc(), "mc")
button_7.connect("clicked", Processing_Digit(), "7")
button_8.connect("clicked", Processing_Digit(), "8")
button_9.connect("clicked", Processing_Digit(), "9")
button_minus.connect("clicked", Processing_OrdinaryOperation(), "-")
button_sqrt.connect("clicked", Processing_NotOrdinaryOperation(), "sqrt")
button_mr.connect("clicked", Processing_Mr(), "mr")
button_4.connect("clicked", Processing_Digit(), "4")
button_5.connect("clicked", Processing_Digit(), "5")
button_6.connect("clicked", Processing_Digit(), "6")
button_multi.connect("clicked", Processing_OrdinaryOperation(), "*")
button_1divx.connect("clicked", Processing_NotOrdinaryOperation(), "1/x")
button_ms.connect("clicked", Processing_Ms(), "ms")
button_1.connect("clicked", Processing_Digit(), "1")
button_2.connect("clicked", Processing_Digit(), "2")
button_3.connect("clicked", Processing_Digit(), "3")
button_div.connect("clicked", Processing_OrdinaryOperation(), "/")
button_powxy.connect("clicked", Processing_OrdinaryOperation(), "**")
button_mplus.connect("clicked", Processing_Mplus(), "m+")
button_0.connect("clicked", Processing_Digit(), "0")
button_00.connect("clicked", Processing_Digit(), "00")
button_comma.connect("clicked", Processing_Comma(), ".")
button_eq.connect("clicked", Processing_Equal(), "=")
button_proc.connect("clicked", Processing_OrdinaryOperation(), "%")
button_minusplus.connect("clicked", Processing_MinusPlus(), "-/+")


pyCulatorWindow = MainWindow()
pyCulatorWindow.show_all()
Gtk.main()