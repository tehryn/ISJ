#!/usr/bin/env python3
# author: Matejka Jiri, FIT VUT
# login: xmatej52
# date: 9 April, 2016
class Polynomial(list): #class
	"""
	class of polynomial
	INITIALIZATION:
		self - object
		self.arg - list of coefficients
	FUNCTIONS:
		__init__(self, *argc, **kwords) - Initialization of Polynomial
		__repr__(self) - Printing the polynomial
		__add__(self, other) - Adding two polynomials, return new polynomial
		__pow__(self, exp) - Exponentiation of polynomial
		derivate(self) - Derivation of polynomial
		at_value(self, *value) - Achieving value for x or solving the integral
	
	"""
################################################################################
	def __init__(self, *argc, **kwords):
		"""
		Initialization of Polynomial
		ARGS:
			self - polynomial for initialization
			*argc - coefficients of x as values
			**kwords - coefficients of x as string
		NOTE:
			self.agr is list of coefficients
		"""
		if kwords:
			keys = sorted(kwords)
			self.arg=list(range(len(keys)))
			i = 0
			#storing values
			for kw in keys:
				self.arg[i]=kwords[kw]
				i = i + 1
			#now we have to find missing values
			y = list(range(len(keys)))
			i = 0
			#separate numbers from string and save it in list y
			for x in keys:
				y[i] = int(x[1:])
#				print(y)
				i = i + 1
			i = 0
			size = len(y)
			#looking for missing values
			while i < size:
#				print(y)
				if (i != y[i]): #missing value found
					y.append(0)
					self.arg.append(0)
					j = len(self.arg) - 1
					while ( j >= i): #moving list
						y[j] = y[j-1]
						self.arg[j] = self.arg[j-1]
						j = j - 1 
					y[i] = i
					self.arg[i] = 0 #inserting coefficient into correct(I hope so) index
					i = i + 1
#					print(y)
				i = i + 1 

		else:
			self.arg = list(range(len(argc)))
			if (type(argc[0]) == type(list())): #if argc is list
				self.arg = list(range(len(argc[0])))
				i = 0
				for x in argc[0]:
					self.arg[i] = x
					i = i + 1
			else:
				self.arg = list(argc)
################################################################################
	def __str__(self):
		"""
		Printing the polynimial
		ARGS:
			self - polynomial that will be print
		RETURN:
			text - string for printing
		"""
		text = ""
		length = len(self.arg)
		i = 0
		for x in self.arg:
			if (x == 0):
				i = i + 1
				continue
			elif (i == 0 and x < 0):
				x = -x
				text = "- %s" % (x) + text
			elif (i == 0):
				text = "+ %s" % (x) + text
			elif (x < 0):
				x = -x
				if (i == 1):
					if (x == 1):
						text = "- x " + text
					else:
						text = "- %sx " % (x) + text
				else:
					if (x == 1):
						text = "- x^%s " % (i) + text
					else:
						text = "- %sx^%s " % (x, i) + text
			else:
				if (i == 1):
					if (x == 1):
						text = "+ x " + text
					else:
						text = "+ %sx " % (x) + text
				else:
					if (x == 1):
						text = "+ x^%s " % (i) + text
					else:
						text = "+ %sx^%s " % (x, i) + text
			i = i + 1
		if not text:
			text = "0"
		if (text[0] == "+"): # fixing mistake + at beginnig
			text = text[2:]
		if (text[-1] == " "): # fixing mistake + at beginnig
			text = text[:-1]
		return text
################################################################################
	def __add__(self, other):
		"""
		Adding two polynomials, return new polynomial
		ARGS:
			self - first polynomial
			other - second polynomial
		RETURN:
			result - new polynomial (sum of self and other)
		"""
		if (len(self.arg) < len(other.arg)):
			summ = Polynomial(other.arg)
			i = len(self.arg) - 1
			for x in self.arg:
				summ.arg[i] = self.arg[i] + summ.arg[i]
				i = i - 1
		else:
			summ = Polynomial(self.arg)
			i = len(other.arg) - 1
			for x in other.arg:
				summ.arg[i] = other.arg[i] + summ.arg[i]
				i = i - 1
		return summ
################################################################################			
	def __pow__(self, exp):
		"""
		Exponentiation of polynomial
		ARGS:
			self - first polynomial
			exp - exponent
		FUNCTIONS:
			mull(self, other) - Multiply two polynomials
		RETURN:
			result - new polynomial (self^exp)
		"""
		def mull(self, other):
			"""
			Multiply two polynomials
			ARGS:
				self - first polynomial, len(self.arg) >= len(other.arg)
				other - second polynomial
			RETURN:
				Polynomial(result) - new polynomial where result is list with coefficients (self * other)
			"""
			size = len(self.arg) - 1 + len(other.arg)
			result = list(range(size))
			i = 0;
			while i<size:
				result[i] = 0
				i = i + 1
			i = 0
			while i<size:
				j = 0
				while j < len(other.arg):
					k = 0
					while k < len(self.arg):
						if i == k + j:
							result[i] = result[i] + self.arg[k]*other.arg[j]
						k = k + 1
					j = j + 1
				i = i + 1
			return Polynomial(result)
		
		if exp == 0:
			return Polynomial(1)
		
		i = 1
		result = self
		while i < exp:
			result = mull(result, self)
			i = i + 1
		return result
################################################################################		
	def derivative(self):
		"""
		Derivation of polynomial
		ARGS:
			self - polynomial for derivation
		RETURN:
			der - new polynomial (derivation of self)
		"""
		length = len(self.arg)
		i = 0
		der = Polynomial(self.arg)
		for x in self.arg:
			der.arg[i] = i * x
			i = i + 1
		del der.arg[0]
		return der
################################################################################
	def at_value(self, *value):
		"""
		Achieving value for x or solving the integral
		ARGS:
			self - polynomial
			*value - values for solving integral or for solving the polynomial
		RETURN:
			result - integer value
		"""
		result = 0
		for x in value:
			i = 0
			for coef in self.arg:
				result = result + coef * (x ** i)
				i = i + 1
			result = -result
		return -result
################################################################################
	def __eq__(self, other):
		"""
		Determination if two polynomials are equal
		ARGS:
			self - first polynomial
			other - second polynomial
		RETURN:
			result - True when equal, otherwise false
		"""
		return (str(self) == str(other))
#		if str(self) == str(other):
#			return True
#		return False
# DEBUG - listed only those from wis, of course I "tested" more cases

#init
#pol1 = Polynomial([1,-3,0,2])
#pol2 = Polynomial(1,-3,0,2)
#pol3 = Polynomial(x0=1,x3=2,x1=-3)

#print
#print(pol1)
#print(pol2)
#print(pol3)
# 2x^3 - 3x + 1
# 2x^3 - 3x + 1
# 2x^3 - 3x + 1

#add
#print(Polynomial(1,-3,0,2) + Polynomial(0, 2, 1))
# 2x^3 + x^2 - x + 1

#exponent
#print(Polynomial(-1, 1) ** 2)
# x^2 - 2x  + 1


#derivative
#print(pol1.derivative())
# 6x^2 - 3

#at_value
#print(pol1.at_value(2))
#print(pol1.at_value(2,3))
# 11
# 35

pol1 = Polynomial(x2=3, x0=1)
pol2 = Polynomial(x1=1, x3=0)
pol3 = Polynomial(x0=-1,x1=1)
pol4 = Polynomial(x3=2,x1=3,x0=2)
pol5 = Polynomial([1,0,-2])
print(str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x")
print(str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5")

print("=================")
print(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1))
print(str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x")
print("=================")


print(str(Polynomial(x2=0)) == "0")
print(str(Polynomial(x0=0)) == "0")
print(str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1")
print(Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3))
print(Polynomial(x2=0) == Polynomial(x0=0))
print(str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2")

print("=================")
print(str(pol1+pol2) == "3x^2 + x + 1")
print(str(pol2+pol1) == "3x^2 + x + 1")
print("=================")

print(str(Polynomial(x0=-1,x1=1)**1) == "x - 1")
print(str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1")
print(str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1")
print(str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1")
print(str(Polynomial(x0=2).derivative()) == "0")
print(str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3")
print(str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x")
print(str(pol4.derivative()) == "6x^2 + 3")
print(str(pol4.derivative()) == "6x^2 + 3")
print(Polynomial(-2,3,4,-5).at_value(0) == -2)
print(Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20)
print(Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44)
print(pol5.at_value(-2.4) == -10.520)
print(pol5.at_value(-2.4) == -10.52)
print(pol5.at_value(-1,3.6) == -23.92)
print(pol5.at_value(-1,3.6) == -23.92)
