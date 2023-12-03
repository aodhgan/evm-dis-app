import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Int

# Module: MiscTypes

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Zip(u, v):
        return _dafny.SeqWithoutIsStrInference([((u)[d_1_i_], (v)[d_1_i_]) for d_1_i_ in range(len(u))])

    @staticmethod
    def UnZip(x):
        d_2_x0_ = _dafny.SeqWithoutIsStrInference([((x)[d_3_i_])[0] for d_3_i_ in range(len(x))])
        d_4_x1_ = _dafny.SeqWithoutIsStrInference([((x)[d_5_i_])[1] for d_5_i_ in range(len(x))])
        return (d_2_x0_, d_4_x1_)

    @staticmethod
    def Filter(u, f):
        d_6___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(u)) == (0):
                    return (d_6___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif f((u)[0]):
                    d_6___accumulator_ = (d_6___accumulator_) + (_dafny.SeqWithoutIsStrInference([(u)[0]]))
                    in1_ = _dafny.SeqWithoutIsStrInference((u)[1::])
                    in2_ = f
                    u = in1_
                    f = in2_
                    raise _dafny.TailCall()
                elif True:
                    in3_ = _dafny.SeqWithoutIsStrInference((u)[1::])
                    in4_ = f
                    u = in3_
                    f = in4_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Exists(xs, f):
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return False
                elif f((xs)[0]):
                    return True
                elif True:
                    in5_ = _dafny.SeqWithoutIsStrInference((xs)[1::])
                    in6_ = f
                    xs = in5_
                    f = in6_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def Map(t, f):
        return _dafny.SeqWithoutIsStrInference([f((t)[d_7_i_]) for d_7_i_ in range(len(t))])

    @staticmethod
    def Find(x, t):
        return default__.FindRec(x, t, 0)

    @staticmethod
    def FindRec(x, t, i):
        while True:
            with _dafny.label():
                if (len(x)) == (0):
                    return Option_None()
                elif ((x)[0]) == (t):
                    return Option_Some(i)
                elif True:
                    in7_ = _dafny.SeqWithoutIsStrInference((x)[1::])
                    in8_ = t
                    in9_ = (i) + (1)
                    x = in7_
                    t = in8_
                    i = in9_
                    raise _dafny.TailCall()
                break


class Try:
    @classmethod
    def default(cls, ):
        return lambda: Try_Failure(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Success(self) -> bool:
        return isinstance(self, Try_Success)
    @property
    def is_Failure(self) -> bool:
        return isinstance(self, Try_Failure)

class Try_Success(Try, NamedTuple('Success', [('v', Any)])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Try.Success({_dafny.string_of(self.v)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Try_Success) and self.v == __o.v
    def __hash__(self) -> int:
        return super().__hash__()

class Try_Failure(Try, NamedTuple('Failure', [('msg', Any)])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Try.Failure({self.msg.VerbatimString(True)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Try_Failure) and self.msg == __o.msg
    def __hash__(self) -> int:
        return super().__hash__()


class Option:
    @classmethod
    def default(cls, ):
        return lambda: Option_None()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_None(self) -> bool:
        return isinstance(self, Option_None)
    @property
    def is_Some(self) -> bool:
        return isinstance(self, Option_Some)
    def Extract(self):
        return (self).v


class Option_None(Option, NamedTuple('None_', [])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Option.None'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_None)
    def __hash__(self) -> int:
        return super().__hash__()

class Option_Some(Option, NamedTuple('Some', [('v', Any)])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Option.Some({_dafny.string_of(self.v)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Option_Some) and self.v == __o.v
    def __hash__(self) -> int:
        return super().__hash__()


class Either:
    @classmethod
    def default(cls, default_T):
        return lambda: Either_Left(default_T())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Left(self) -> bool:
        return isinstance(self, Either_Left)
    @property
    def is_Right(self) -> bool:
        return isinstance(self, Either_Right)
    def Left(self):
        return (self).l

    def Right(self):
        return (self).r


class Either_Left(Either, NamedTuple('Left', [('l', Any)])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Either.Left({_dafny.string_of(self.l)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Either_Left) and self.l == __o.l
    def __hash__(self) -> int:
        return super().__hash__()

class Either_Right(Either, NamedTuple('Right', [('r', Any)])):
    def __dafnystr__(self) -> str:
        return f'MiscTypes.Either.Right({_dafny.string_of(self.r)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Either_Right) and self.r == __o.r
    def __hash__(self) -> int:
        return super().__hash__()

