import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Int
import MiscTypes
import EVMConstants
import EVMOpcodes
import OpcodeDecoder
import Hex
import StackElement
import WeakPre
import State
import EVMToolTips
import Instructions
import BinaryDecoder
import LinSegments
import Splitter
import SegBuilder
import ProofObject
import PrettyIns
import PrettyPrinters
import ProofObjectBuilder
import ArgParser
import SeqOfSets
import PartitionMod
import Automata
import Minimiser

# Module: CFGraph

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def BoolSeqToNat(xb):
        if (len(xb)) == (0):
            return 0
        elif True:
            return ((1 if (xb)[0] else 0)) + ((2) * (default__.BoolSeqToNat(_dafny.SeqWithoutIsStrInference((xb)[1::]))))

    @staticmethod
    def SegNumPartition(p, m, maxSegNum, n):
        while True:
            with _dafny.label():
                if (n) <= (maxSegNum):
                    def lambda51_(d_837_m_, d_838_n_, d_839_p_):
                        def lambda52_(d_840_x_):
                            return (((d_837_m_)[d_840_x_]).seg) == (MiscTypes.Option_Some(d_838_n_))

                        return lambda52_

                    d_836_f_ = lambda51_(m, n, p)
                    d_841_p1_ = (p).SplitAt(d_836_f_, (len((p).elem)) - (1))
                    in108_ = d_841_p1_
                    in109_ = m
                    in110_ = maxSegNum
                    in111_ = (n) + (1)
                    p = in108_
                    m = in109_
                    maxSegNum = in110_
                    n = in111_
                    raise _dafny.TailCall()
                elif True:
                    return p
                break

    @staticmethod
    def EdgesToMap(edges, seenNodes, reverseSeenNodes, builtMap, lastNum, index):
        while True:
            with _dafny.label():
                if (len(edges)) == (index):
                    return (lastNum, builtMap, seenNodes, reverseSeenNodes)
                elif True:
                    let_tmp_rhs0_ = (((seenNodes)[((edges)[index]).src], lastNum, seenNodes, reverseSeenNodes) if (((edges)[index]).src) in ((seenNodes).keys) else ((lastNum) + (1), (lastNum) + (1), (seenNodes).set(((edges)[index]).src, (lastNum) + (1)), (reverseSeenNodes).set((lastNum) + (1), ((edges)[index]).src)))
                    d_842_src_ = let_tmp_rhs0_[0]
                    d_843_last_ = let_tmp_rhs0_[1]
                    d_844_m1_ = let_tmp_rhs0_[2]
                    d_845_rm1_ = let_tmp_rhs0_[3]
                    let_tmp_rhs1_ = (((d_844_m1_)[((edges)[index]).tgt], d_843_last_, d_844_m1_, d_845_rm1_) if (((edges)[index]).tgt) in ((d_844_m1_).keys) else ((d_843_last_) + (1), (d_843_last_) + (1), (d_844_m1_).set(((edges)[index]).tgt, (d_843_last_) + (1)), (d_845_rm1_).set((d_843_last_) + (1), ((edges)[index]).tgt)))
                    d_846_tgt_ = let_tmp_rhs1_[0]
                    d_847_last_k_ = let_tmp_rhs1_[1]
                    d_848_m2_ = let_tmp_rhs1_[2]
                    d_849_rm2_ = let_tmp_rhs1_[3]
                    d_850_b_ = (builtMap).set((d_842_src_, ((edges)[index]).lab), d_846_tgt_)
                    in112_ = edges
                    in113_ = d_848_m2_
                    in114_ = d_849_rm2_
                    in115_ = d_850_b_
                    in116_ = d_847_last_k_
                    in117_ = (index) + (1)
                    edges = in112_
                    seenNodes = in113_
                    reverseSeenNodes = in114_
                    builtMap = in115_
                    lastNum = in116_
                    index = in117_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def BoolsToString(x):
        d_851___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(x)) == (0):
                    return (d_851___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "E")))
                elif True:
                    d_851___accumulator_ = (d_851___accumulator_) + (_dafny.SeqWithoutIsStrInference([(_dafny.CodePoint('1') if (x)[0] else _dafny.CodePoint('0'))]))
                    in118_ = _dafny.SeqWithoutIsStrInference((x)[1::])
                    x = in118_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def SegColour(s):
        source64_ = s
        if source64_.is_JUMPSeg:
            d_852___mcc_h0_ = source64_.ins
            d_853___mcc_h1_ = source64_.lastIns
            d_854___mcc_h2_ = source64_.netOpEffect
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif source64_.is_JUMPISeg:
            d_855___mcc_h6_ = source64_.ins
            d_856___mcc_h7_ = source64_.lastIns
            d_857___mcc_h8_ = source64_.netOpEffect
            return default__.branchColour
        elif source64_.is_RETURNSeg:
            d_858___mcc_h12_ = source64_.ins
            d_859___mcc_h13_ = source64_.lastIns
            d_860___mcc_h14_ = source64_.netOpEffect
            return default__.returnColour
        elif source64_.is_STOPSeg:
            d_861___mcc_h18_ = source64_.ins
            d_862___mcc_h19_ = source64_.lastIns
            d_863___mcc_h20_ = source64_.netOpEffect
            return default__.revertColour
        elif source64_.is_CONTSeg:
            d_864___mcc_h24_ = source64_.ins
            d_865___mcc_h25_ = source64_.lastIns
            d_866___mcc_h26_ = source64_.netOpEffect
            return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        elif True:
            d_867___mcc_h30_ = source64_.ins
            d_868___mcc_h31_ = source64_.lastIns
            d_869___mcc_h32_ = source64_.netOpEffect
            return default__.invalidColour

    @staticmethod
    def DOTSeg(s, numSeg):
        d_870_prefix_ = ((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<B>Segment "))) + (Int.default__.NatToString(numSeg))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [0x")))) + (Hex.default__.NatToHex((s).StartAddress()))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "]</B><BR ALIGN=\"CENTER\"/>\n")))
        d_871_body_ = default__.DOTIns((s).Ins())
        return (d_870_prefix_) + (d_871_body_)

    @staticmethod
    def DOTSegTable(s, numSeg):
        d_872_tableStart_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<TABLE ALIGN=\"LEFT\" CELLBORDER=\"0\" BORDER=\"0\" cellpadding=\"0\"  CELLSPACING=\"1\">\n"))
        d_873_prefix_ = (((((((((((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<TR><TD "))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ">Segment ")))) + (Int.default__.NatToString(numSeg))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [0x")))) + (Hex.default__.NatToHex((s).StartAddress()))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "]</TD>")))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<TD")))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " href=\"\" tooltip=\"Stack Size &#916;: ")))) + (Int.default__.IntToString((s).StackEffect()))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "  -- Operands &#8805; ")))) + (Int.default__.NatToString((s).WeakestPreOperands(0)))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\"")))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ">&#128218;</TD>")))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "</TR><HR/>\n")))
        d_874_tableEnd_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "</TABLE>\n"))
        d_875_body_ = default__.DOTInsTable((s).Ins(), True)
        return (((d_872_tableStart_) + (d_873_prefix_)) + (d_875_body_)) + (d_874_tableEnd_)

    @staticmethod
    def DOTIns(xi):
        d_876___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(xi)) == (0):
                    return (d_876___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_877_a_ = (((xi)[0]).ToString()) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " <BR ALIGN=\"LEFT\"/>\n")))
                    d_876___accumulator_ = (d_876___accumulator_) + (d_877_a_)
                    in119_ = _dafny.SeqWithoutIsStrInference((xi)[1::])
                    xi = in119_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def DOTInsTable(xi, isFirst):
        d_878___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(xi)) == (0):
                    return (d_878___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                elif True:
                    d_879_prefix_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<TR><TD width=\"1\" fixedsize=\"true\" align=\"left\">\n"))
                    d_880_suffix_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "</TD></TR>\n"))
                    d_881_exitPortTag_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "PORT=\"exit\"")) if ((xi)[0]).IsJump() else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                    d_882_entryPortTag_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "PORT=\"entry\"")) if isFirst else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                    d_883_a_ = ((xi)[0]).ToHTMLTable(d_882_entryPortTag_, d_881_exitPortTag_)
                    d_878___accumulator_ = (d_878___accumulator_) + (((d_879_prefix_) + (d_883_a_)) + (d_880_suffix_))
                    in120_ = _dafny.SeqWithoutIsStrInference((xi)[1::])
                    in121_ = False
                    xi = in120_
                    isFirst = in121_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def NatBoolEdgesToCFGEdges(xs, m, maxSegNum):
        d_884___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        while True:
            with _dafny.label():
                if (len(xs)) == (0):
                    return (d_884___accumulator_) + (_dafny.SeqWithoutIsStrInference([]))
                elif True:
                    d_884___accumulator_ = (d_884___accumulator_) + (_dafny.SeqWithoutIsStrInference([BoolEdge_BoolEdge((m)[((xs)[0])[0]], ((xs)[0])[1], (m)[((xs)[0])[2]])]))
                    in122_ = _dafny.SeqWithoutIsStrInference((xs)[1::])
                    in123_ = m
                    in124_ = maxSegNum
                    xs = in122_
                    m = in123_
                    maxSegNum = in124_
                    raise _dafny.TailCall()
                break

    @_dafny.classproperty
    def jcolour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "royalblue"))
    @_dafny.classproperty
    def jumpColour(instance):
        return ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "color="))) + (default__.jcolour)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ",")))
    @_dafny.classproperty
    def skcolour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "black"))
    @_dafny.classproperty
    def skipColour(instance):
        return ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "color="))) + (default__.skcolour)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ",")))
    @_dafny.classproperty
    def revertColour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "style=filled,color=orange,fontcolor=white,"))
    @_dafny.classproperty
    def returnColour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "style=filled,color=olivedrab,fontcolor=white,"))
    @_dafny.classproperty
    def invalidColour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "style=filled,color=firebrick,fontcolor=white,"))
    @_dafny.classproperty
    def branchColour(instance):
        return _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))

class CFGNode:
    @classmethod
    def default(cls, ):
        return lambda: CFGNode_CFGNode(_dafny.Seq({}), MiscTypes.Option.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_CFGNode(self) -> bool:
        return isinstance(self, CFGNode_CFGNode)
    def ToString(self):
        return default__.BoolsToString((self).id)

    def ToDot(self):
        d_885_x_ = default__.BoolSeqToNat((self).id)
        return ((Int.default__.NatToString(d_885_x_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "_")))) + (Int.default__.NatToString(len((self).id)))


class CFGNode_CFGNode(CFGNode, NamedTuple('CFGNode', [('id', Any), ('seg', Any)])):
    def __dafnystr__(self) -> str:
        return f'CFGraph.CFGNode.CFGNode({_dafny.string_of(self.id)}, {_dafny.string_of(self.seg)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, CFGNode_CFGNode) and self.id == __o.id and self.seg == __o.seg
    def __hash__(self) -> int:
        return super().__hash__()


class BoolEdge:
    @classmethod
    def default(cls, ):
        return lambda: BoolEdge_BoolEdge(CFGNode.default()(), False, CFGNode.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BoolEdge(self) -> bool:
        return isinstance(self, BoolEdge_BoolEdge)
    def DOTPrint2(self):
        d_886_lab1_ = (((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<FONT color=\""))) + (default__.jcolour)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\">jump</FONT>"))) if (self).lab else ((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "<FONT color=\""))) + (default__.skcolour)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "\">skip</FONT>"))))
        d_887_labColour_ = (default__.jumpColour if (self).lab else default__.skipColour)
        return ((((((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s"))) + (((self).src).ToDot())) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " -> s")))) + (((self).tgt).ToDot())) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [")))) + (d_887_labColour_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "label=<")))) + (d_886_lab1_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ">]\n")))

    def DOTPrint(self, fancyExit):
        d_888_lab1_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "tooltip=\"Jump\",style=dashed")) if (self).lab else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "tooltip=\"Next\"")))
        d_889_labColour_ = (default__.jumpColour if (self).lab else default__.skipColour)
        d_890_exitPort_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ":exit:se ")) if (fancyExit) and ((self).lab) else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
        d_891_entryPort_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ":entry:w ")) if (fancyExit) and ((self).lab) else _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
        return ((((((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s"))) + (((self).src).ToDot())) + (d_890_exitPort_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " -> s")))) + (((self).tgt).ToDot())) + (d_891_entryPort_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [")))) + (d_888_lab1_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "]\n")))


class BoolEdge_BoolEdge(BoolEdge, NamedTuple('BoolEdge', [('src', Any), ('lab', Any), ('tgt', Any)])):
    def __dafnystr__(self) -> str:
        return f'CFGraph.BoolEdge.BoolEdge({_dafny.string_of(self.src)}, {_dafny.string_of(self.lab)}, {_dafny.string_of(self.tgt)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoolEdge_BoolEdge) and self.src == __o.src and self.lab == __o.lab and self.tgt == __o.tgt
    def __hash__(self) -> int:
        return super().__hash__()


class BoolCFGraph:
    @classmethod
    def default(cls, ):
        return lambda: BoolCFGraph_BoolCFGraph(_dafny.Seq({}), int(0))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_BoolCFGraph(self) -> bool:
        return isinstance(self, BoolCFGraph_BoolCFGraph)
    def AddEdge(self, e):
        return BoolCFGraph_BoolCFGraph((_dafny.SeqWithoutIsStrInference([e])) + ((self).edges), 0)

    def IsValid(self):
        def lambda53_(forall_var_10_):
            d_892_k_: int = forall_var_10_
            return not (((0) <= (d_892_k_)) and ((d_892_k_) < (len((self).edges)))) or (not ((((((self).edges)[d_892_k_]).src).seg).is_Some) or (((((((self).edges)[d_892_k_]).src).seg).v) <= ((self).maxSegNum)))

        def lambda54_(forall_var_11_):
            d_893_k_: int = forall_var_11_
            return not (((0) <= (d_893_k_)) and ((d_893_k_) < (len((self).edges)))) or (not ((((((self).edges)[d_893_k_]).tgt).seg).is_Some) or (((((((self).edges)[d_893_k_]).tgt).seg).v) <= ((self).maxSegNum)))

        return (_dafny.quantifier(_dafny.IntegerRange(0, len((self).edges)), True, lambda53_)) and (_dafny.quantifier(_dafny.IntegerRange(0, len((self).edges)), True, lambda54_))

    def Minimise(self):
        d_894_r_ = default__.EdgesToMap((self).edges, _dafny.Map({CFGNode_CFGNode(_dafny.SeqWithoutIsStrInference([]), MiscTypes.Option_Some(0)): 0}), _dafny.Map({0: CFGNode_CFGNode(_dafny.SeqWithoutIsStrInference([]), MiscTypes.Option_Some(0))}), _dafny.Map({}), 0, 0)
        d_895_idToNum_ = (d_894_r_)[2]
        d_896_numToCFGNode_ = (d_894_r_)[3]
        d_897_lastStateNum_ = (d_894_r_)[0]
        d_898_transitions_ = (d_894_r_)[1]
        d_899_a_ = Automata.Auto_Auto((d_897_lastStateNum_) + (1), d_898_transitions_)
        if (d_897_lastStateNum_) > (0):
            def iife16_():
                coll1_ = _dafny.Set()
                compr_1_: int
                for compr_1_ in _dafny.IntegerRange(0, (d_897_lastStateNum_) + (1)):
                    d_901_q_: int = compr_1_
                    if ((0) <= (d_901_q_)) and ((d_901_q_) < ((d_897_lastStateNum_) + (1))):
                        coll1_ = coll1_.union(_dafny.Set([d_901_q_]))
                return _dafny.Set(coll1_)
            d_900_s_ = iife16_()

            d_902_p_ = PartitionMod.Partition_Partition((d_897_lastStateNum_) + (1), _dafny.SeqWithoutIsStrInference([d_900_s_]))
            d_903_p1_ = default__.SegNumPartition(d_902_p_, d_896_numToCFGNode_, (self).maxSegNum, 0)
            d_904_vp_ = Minimiser.Pair_Pair(d_899_a_, d_903_p1_)
            d_905_minim_ = Minimiser.default__.Minimise(d_904_vp_)
            d_906_listOfEdges_ = (d_905_minim_).GenerateReduced(0)
            d_907_x_ = default__.NatBoolEdgesToCFGEdges(d_906_listOfEdges_, d_896_numToCFGNode_, (self).maxSegNum)
            d_908_miniCFG_ = BoolCFGraph_BoolCFGraph(d_907_x_, (self).maxSegNum)
            return d_908_miniCFG_
        elif True:
            return BoolCFGraph_BoolCFGraph(_dafny.SeqWithoutIsStrInference([]), (self).maxSegNum)

    def DOTPrintEdges(self, xe, fancyExits):
        d_909___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        _this = self
        while True:
            with _dafny.label():
                if (len(xe)) > (0):
                    d_909___accumulator_ = (d_909___accumulator_) + (((xe)[0]).DOTPrint(False))
                    in125_ = _this
                    in126_ = _dafny.SeqWithoutIsStrInference((xe)[1::])
                    in127_ = fancyExits
                    _this = in125_
                    
                    xe = in126_
                    fancyExits = in127_
                    raise _dafny.TailCall()
                elif True:
                    return (d_909___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                break

    def DOTPrintNodes(self, xs, g, printed):
        d_910___accumulator_ = _dafny.SeqWithoutIsStrInference([])
        _this = self
        while True:
            with _dafny.label():
                if (len(g)) > (0):
                    d_911_srctxt_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")) if (((g)[0]).src) in (printed) else (((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s"))) + ((((g)[0]).src).ToDot())) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "[label=<ErrorEnd <BR ALIGN=\"CENTER\"/>>]\n"))) if ((((g)[0]).src).seg).is_None else (_this).DOTPrintNodeLabel(((g)[0]).src, (xs)[((((g)[0]).src).seg).v])))
                    d_912_tgttxt_ = (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")) if (((g)[0]).tgt) in (printed) else (((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s"))) + ((((g)[0]).tgt).ToDot())) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "[label=<ErrorEnd <BR ALIGN=\"CENTER\"/>>]\n"))) if ((((g)[0]).tgt).seg).is_None else (_this).DOTPrintNodeLabel(((g)[0]).tgt, (xs)[((((g)[0]).tgt).seg).v])))
                    d_910___accumulator_ = (d_910___accumulator_) + ((d_911_srctxt_) + (d_912_tgttxt_))
                    in128_ = _this
                    in129_ = xs
                    in130_ = _dafny.SeqWithoutIsStrInference((g)[1::])
                    in131_ = (printed) | (_dafny.Set({((g)[0]).src, ((g)[0]).tgt}))
                    _this = in128_
                    
                    xs = in129_
                    g = in130_
                    printed = in131_
                    raise _dafny.TailCall()
                elif True:
                    return (d_910___accumulator_) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "")))
                break

    def DOTPrintNodeLabel(self, n, s):
        d_913_lab_ = default__.DOTSegTable(s, ((n).seg).v)
        d_914_nodeColour_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ""))
        return ((((((_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "s"))) + ((n).ToDot())) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, " [")))) + (d_914_nodeColour_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "label=<\n")))) + (d_913_lab_)) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, ">]\n")))

    def DOTPrint(self, xs, fancyExits):
        d_915_prefix_ = _dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "digraph CFG {\nnode [shape=box]\nnode[fontname=arial]\nedge[fontname=arial]\nranking=TB\n "))
        return (((d_915_prefix_) + ((self).DOTPrintNodes(xs, (self).edges, _dafny.Set({})))) + ((self).DOTPrintEdges((self).edges, fancyExits))) + (_dafny.SeqWithoutIsStrInference(map(_dafny.CodePoint, "}\n")))


class BoolCFGraph_BoolCFGraph(BoolCFGraph, NamedTuple('BoolCFGraph', [('edges', Any), ('maxSegNum', Any)])):
    def __dafnystr__(self) -> str:
        return f'CFGraph.BoolCFGraph.BoolCFGraph({_dafny.string_of(self.edges)}, {_dafny.string_of(self.maxSegNum)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoolCFGraph_BoolCFGraph) and self.edges == __o.edges and self.maxSegNum == __o.maxSegNum
    def __hash__(self) -> int:
        return super().__hash__()

