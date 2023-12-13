import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import MiscTypes

# Module: Int

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Abs(x):
        if (x) >= (0):
            return x
        elif True:
            return (0) - (x)

    @staticmethod
    def Max(i1, i2):
        if (i1) >= (i2):
            return i1
        elif True:
            return i2

    @staticmethod
    def Min(i1, i2):
        if (i1) < (i2):
            return i1
        elif True:
            return i2

    @staticmethod
    def NatToString(n):
        d_7___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (n) < (10):
                    return (_dafny.SeqWithoutIsStrInference([default__.DigitToString(n)])) + (d_7___accumulator_)
                elif True:
                    d_7___accumulator_ = (_dafny.SeqWithoutIsStrInference([default__.DigitToString(_dafny.euclidian_modulus(n, 10))])) + (d_7___accumulator_)
                    in9_ = _dafny.euclidian_division(n, 10)
                    n = in9_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def IntToString(n):
        if (n) == (0):
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "0"))
        elif (n) > (0):
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "+"))) + (default__.NatToString(n))
        elif True:
            return (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "-"))) + (default__.NatToString((0) - (n)))

    @staticmethod
    def DigitToString(n):
        if (n) == (0):
            return _dafny.CodePoint('0')
        elif (n) == (1):
            return _dafny.CodePoint('1')
        elif (n) == (2):
            return _dafny.CodePoint('2')
        elif (n) == (3):
            return _dafny.CodePoint('3')
        elif (n) == (4):
            return _dafny.CodePoint('4')
        elif (n) == (5):
            return _dafny.CodePoint('5')
        elif (n) == (6):
            return _dafny.CodePoint('6')
        elif (n) == (7):
            return _dafny.CodePoint('7')
        elif (n) == (8):
            return _dafny.CodePoint('8')
        elif True:
            return _dafny.CodePoint('9')

    @staticmethod
    def CharToDigit(c):
        if (c) == (_dafny.CodePoint('0')):
            return MiscTypes.Option_Some(0)
        elif (c) == (_dafny.CodePoint('1')):
            return MiscTypes.Option_Some(1)
        elif (c) == (_dafny.CodePoint('2')):
            return MiscTypes.Option_Some(2)
        elif (c) == (_dafny.CodePoint('3')):
            return MiscTypes.Option_Some(3)
        elif (c) == (_dafny.CodePoint('4')):
            return MiscTypes.Option_Some(4)
        elif (c) == (_dafny.CodePoint('5')):
            return MiscTypes.Option_Some(5)
        elif (c) == (_dafny.CodePoint('6')):
            return MiscTypes.Option_Some(6)
        elif (c) == (_dafny.CodePoint('7')):
            return MiscTypes.Option_Some(7)
        elif (c) == (_dafny.CodePoint('8')):
            return MiscTypes.Option_Some(8)
        elif (c) == (_dafny.CodePoint('9')):
            return MiscTypes.Option_Some(9)
        elif True:
            return MiscTypes.Option_None()

    @staticmethod
    def IsNatNumber(s):
        while True:
            with _dafny.label():
                if (len(s)) == (1):
                    return (default__.CharToDigit((s)[0])).is_Some
                elif True:
                    source0_ = default__.CharToDigit((s)[0])
                    if source0_.is_None:
                        return False
                    elif True:
                        d_8___mcc_h0_ = source0_.v
                        d_9_v_ = d_8___mcc_h0_
                        in10_ = _dafny.SeqWithoutIsStrInference((s)[1::])
                        s = in10_
                        raise _dafny.TailCall()
                break

    @staticmethod
    def StringToNat(s, lastVal):
        if (len(s)) == (1):
            return (default__.CharToDigit((s)[0])).v
        elif True:
            d_10_v_ = (default__.CharToDigit((s)[(len(s)) - (1)])).v
            return (d_10_v_) + ((10) * (default__.StringToNat(_dafny.SeqWithoutIsStrInference((s)[:(len(s)) - (1):]), 0)))

    @_dafny.classproperty
    def TWO__8(instance):
        return 256
    @_dafny.classproperty
    def MAX__U8(instance):
        return (default__.TWO__8) - (1)
    @_dafny.classproperty
    def TWO__16(instance):
        return 65536
    @_dafny.classproperty
    def MAX__U16(instance):
        return (default__.TWO__16) - (1)
    @_dafny.classproperty
    def TWO__32(instance):
        return 4294967296
    @_dafny.classproperty
    def MAX__U32(instance):
        return (default__.TWO__32) - (1)
    @_dafny.classproperty
    def TWO__64(instance):
        return 18446744073709551616
    @_dafny.classproperty
    def MAX__U64(instance):
        return (default__.TWO__64) - (1)
    @_dafny.classproperty
    def TWO__128(instance):
        return 340282366920938463463374607431768211456
    @_dafny.classproperty
    def MAX__U128(instance):
        return (default__.TWO__128) - (1)
    @_dafny.classproperty
    def TWO__256(instance):
        return 115792089237316195423570985008687907853269984665640564039457584007913129639936
    @_dafny.classproperty
    def MAX__U256(instance):
        return (default__.TWO__256) - (1)
    @_dafny.classproperty
    def TWO__4(instance):
        return 16

class u8:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class u16:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class u32:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class u64:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class u128:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)

class u256:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return int(0)
