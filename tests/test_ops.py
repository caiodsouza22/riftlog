import riftlog  # noqa: F401
from riftlog.application.catalog import GLOBAL


def test_math_affine_001():
    fn = GLOBAL.get('math.affine_001')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 2 + -2)

def test_math_affine_002():
    fn = GLOBAL.get('math.affine_002')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 3 + -1)

def test_math_affine_003():
    fn = GLOBAL.get('math.affine_003')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 4 + 0)

def test_math_affine_004():
    fn = GLOBAL.get('math.affine_004')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 5 + 1)

def test_math_affine_005():
    fn = GLOBAL.get('math.affine_005')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 6 + 2)

def test_math_affine_006():
    fn = GLOBAL.get('math.affine_006')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 7 + 3)

def test_math_affine_007():
    fn = GLOBAL.get('math.affine_007')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 8 + -3)

def test_math_affine_008():
    fn = GLOBAL.get('math.affine_008')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 9 + -2)

def test_math_affine_009():
    fn = GLOBAL.get('math.affine_009')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 10 + -1)

def test_math_affine_010():
    fn = GLOBAL.get('math.affine_010')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 11 + 0)

def test_math_affine_011():
    fn = GLOBAL.get('math.affine_011')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 1 + 1)

def test_math_affine_012():
    fn = GLOBAL.get('math.affine_012')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 2 + 2)

def test_math_affine_013():
    fn = GLOBAL.get('math.affine_013')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 3 + 3)

def test_math_affine_014():
    fn = GLOBAL.get('math.affine_014')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 4 + -3)

def test_math_affine_015():
    fn = GLOBAL.get('math.affine_015')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 5 + -2)

def test_math_affine_016():
    fn = GLOBAL.get('math.affine_016')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 6 + -1)

def test_math_affine_017():
    fn = GLOBAL.get('math.affine_017')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 7 + 0)

def test_math_affine_018():
    fn = GLOBAL.get('math.affine_018')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 8 + 1)

def test_math_affine_019():
    fn = GLOBAL.get('math.affine_019')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 9 + 2)

def test_math_affine_020():
    fn = GLOBAL.get('math.affine_020')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 10 + 3)

def test_math_affine_021():
    fn = GLOBAL.get('math.affine_021')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 11 + -3)

def test_math_affine_022():
    fn = GLOBAL.get('math.affine_022')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 1 + -2)

def test_math_affine_023():
    fn = GLOBAL.get('math.affine_023')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 2 + -1)

def test_math_affine_024():
    fn = GLOBAL.get('math.affine_024')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 3 + 0)

def test_math_affine_025():
    fn = GLOBAL.get('math.affine_025')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 4 + 1)

def test_math_affine_026():
    fn = GLOBAL.get('math.affine_026')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 5 + 2)

def test_math_affine_027():
    fn = GLOBAL.get('math.affine_027')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 6 + 3)

def test_math_affine_028():
    fn = GLOBAL.get('math.affine_028')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 7 + -3)

def test_math_affine_029():
    fn = GLOBAL.get('math.affine_029')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 8 + -2)

def test_math_affine_030():
    fn = GLOBAL.get('math.affine_030')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 9 + -1)

def test_math_affine_031():
    fn = GLOBAL.get('math.affine_031')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 10 + 0)

def test_math_affine_032():
    fn = GLOBAL.get('math.affine_032')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 11 + 1)

def test_math_affine_033():
    fn = GLOBAL.get('math.affine_033')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 1 + 2)

def test_math_affine_034():
    fn = GLOBAL.get('math.affine_034')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 2 + 3)

def test_math_affine_035():
    fn = GLOBAL.get('math.affine_035')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 3 + -3)

def test_math_affine_036():
    fn = GLOBAL.get('math.affine_036')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 4 + -2)

def test_math_affine_037():
    fn = GLOBAL.get('math.affine_037')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 5 + -1)

def test_math_affine_038():
    fn = GLOBAL.get('math.affine_038')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 6 + 0)

def test_math_affine_039():
    fn = GLOBAL.get('math.affine_039')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 7 + 1)

def test_math_affine_040():
    fn = GLOBAL.get('math.affine_040')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 8 + 2)

def test_math_affine_041():
    fn = GLOBAL.get('math.affine_041')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 9 + 3)

def test_math_affine_042():
    fn = GLOBAL.get('math.affine_042')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 10 + -3)

def test_math_affine_043():
    fn = GLOBAL.get('math.affine_043')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 11 + -2)

def test_math_affine_044():
    fn = GLOBAL.get('math.affine_044')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 1 + -1)

def test_math_affine_045():
    fn = GLOBAL.get('math.affine_045')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 2 + 0)

def test_math_affine_046():
    fn = GLOBAL.get('math.affine_046')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 3 + 1)

def test_math_affine_047():
    fn = GLOBAL.get('math.affine_047')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 4 + 2)

def test_math_affine_048():
    fn = GLOBAL.get('math.affine_048')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 5 + 3)

def test_math_affine_049():
    fn = GLOBAL.get('math.affine_049')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 6 + -3)

def test_math_affine_050():
    fn = GLOBAL.get('math.affine_050')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 7 + -2)

def test_math_affine_051():
    fn = GLOBAL.get('math.affine_051')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 8 + -1)

def test_math_affine_052():
    fn = GLOBAL.get('math.affine_052')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 9 + 0)

def test_math_affine_053():
    fn = GLOBAL.get('math.affine_053')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 10 + 1)

def test_math_affine_054():
    fn = GLOBAL.get('math.affine_054')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 11 + 2)

def test_math_affine_055():
    fn = GLOBAL.get('math.affine_055')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 1 + 3)

def test_math_affine_056():
    fn = GLOBAL.get('math.affine_056')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 2 + -3)

def test_math_affine_057():
    fn = GLOBAL.get('math.affine_057')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 3 + -2)

def test_math_affine_058():
    fn = GLOBAL.get('math.affine_058')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 4 + -1)

def test_math_affine_059():
    fn = GLOBAL.get('math.affine_059')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 5 + 0)

def test_math_affine_060():
    fn = GLOBAL.get('math.affine_060')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 6 + 1)

def test_math_affine_061():
    fn = GLOBAL.get('math.affine_061')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 7 + 2)

def test_math_affine_062():
    fn = GLOBAL.get('math.affine_062')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 8 + 3)

def test_math_affine_063():
    fn = GLOBAL.get('math.affine_063')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 9 + -3)

def test_math_affine_064():
    fn = GLOBAL.get('math.affine_064')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 10 + -2)

def test_math_affine_065():
    fn = GLOBAL.get('math.affine_065')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 11 + -1)

def test_math_affine_066():
    fn = GLOBAL.get('math.affine_066')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 1 + 0)

def test_math_affine_067():
    fn = GLOBAL.get('math.affine_067')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 2 + 1)

def test_math_affine_068():
    fn = GLOBAL.get('math.affine_068')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 3 + 2)

def test_math_affine_069():
    fn = GLOBAL.get('math.affine_069')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 4 + 3)

def test_math_affine_070():
    fn = GLOBAL.get('math.affine_070')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 5 + -3)

def test_math_affine_071():
    fn = GLOBAL.get('math.affine_071')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 6 + -2)

def test_math_affine_072():
    fn = GLOBAL.get('math.affine_072')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 7 + -1)

def test_math_affine_073():
    fn = GLOBAL.get('math.affine_073')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 8 + 0)

def test_math_affine_074():
    fn = GLOBAL.get('math.affine_074')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 9 + 1)

def test_math_affine_075():
    fn = GLOBAL.get('math.affine_075')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 10 + 2)

def test_math_affine_076():
    fn = GLOBAL.get('math.affine_076')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 11 + 3)

def test_math_affine_077():
    fn = GLOBAL.get('math.affine_077')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 1 + -3)

def test_math_affine_078():
    fn = GLOBAL.get('math.affine_078')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 2 + -2)

def test_math_affine_079():
    fn = GLOBAL.get('math.affine_079')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 3 + -1)

def test_math_affine_080():
    fn = GLOBAL.get('math.affine_080')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 4 + 0)

def test_math_affine_081():
    fn = GLOBAL.get('math.affine_081')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 5 + 1)

def test_math_affine_082():
    fn = GLOBAL.get('math.affine_082')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 6 + 2)

def test_math_affine_083():
    fn = GLOBAL.get('math.affine_083')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 7 + 3)

def test_math_affine_084():
    fn = GLOBAL.get('math.affine_084')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 8 + -3)

def test_math_affine_085():
    fn = GLOBAL.get('math.affine_085')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 9 + -2)

def test_math_affine_086():
    fn = GLOBAL.get('math.affine_086')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 10 + -1)

def test_math_affine_087():
    fn = GLOBAL.get('math.affine_087')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 11 + 0)

def test_math_affine_088():
    fn = GLOBAL.get('math.affine_088')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 1 + 1)

def test_math_affine_089():
    fn = GLOBAL.get('math.affine_089')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 2 + 2)

def test_math_affine_090():
    fn = GLOBAL.get('math.affine_090')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 3 + 3)

def test_math_affine_091():
    fn = GLOBAL.get('math.affine_091')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 4 + -3)

def test_math_affine_092():
    fn = GLOBAL.get('math.affine_092')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 5 + -2)

def test_math_affine_093():
    fn = GLOBAL.get('math.affine_093')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 6 + -1)

def test_math_affine_094():
    fn = GLOBAL.get('math.affine_094')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 7 + 0)

def test_math_affine_095():
    fn = GLOBAL.get('math.affine_095')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 8 + 1)

def test_math_affine_096():
    fn = GLOBAL.get('math.affine_096')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 9 + 2)

def test_math_affine_097():
    fn = GLOBAL.get('math.affine_097')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 10 + 3)

def test_math_affine_098():
    fn = GLOBAL.get('math.affine_098')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 11 + -3)

def test_math_affine_099():
    fn = GLOBAL.get('math.affine_099')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 1 + -2)

def test_math_affine_100():
    fn = GLOBAL.get('math.affine_100')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 2 + -1)

def test_math_affine_101():
    fn = GLOBAL.get('math.affine_101')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 3 + 0)

def test_math_affine_102():
    fn = GLOBAL.get('math.affine_102')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 4 + 1)

def test_math_affine_103():
    fn = GLOBAL.get('math.affine_103')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 5 + 2)

def test_math_affine_104():
    fn = GLOBAL.get('math.affine_104')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 6 + 3)

def test_math_affine_105():
    fn = GLOBAL.get('math.affine_105')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 7 + -3)

def test_math_affine_106():
    fn = GLOBAL.get('math.affine_106')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 8 + -2)

def test_math_affine_107():
    fn = GLOBAL.get('math.affine_107')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 9 + -1)

def test_math_affine_108():
    fn = GLOBAL.get('math.affine_108')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 10 + 0)

def test_math_affine_109():
    fn = GLOBAL.get('math.affine_109')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 11 + 1)

def test_math_affine_110():
    fn = GLOBAL.get('math.affine_110')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 1 + 2)

def test_math_affine_111():
    fn = GLOBAL.get('math.affine_111')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 2 + 3)

def test_math_affine_112():
    fn = GLOBAL.get('math.affine_112')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 3 + -3)

def test_math_affine_113():
    fn = GLOBAL.get('math.affine_113')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 4 + -2)

def test_math_affine_114():
    fn = GLOBAL.get('math.affine_114')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 5 + -1)

def test_math_affine_115():
    fn = GLOBAL.get('math.affine_115')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 6 + 0)

def test_math_affine_116():
    fn = GLOBAL.get('math.affine_116')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 7 + 1)

def test_math_affine_117():
    fn = GLOBAL.get('math.affine_117')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 8 + 2)

def test_math_affine_118():
    fn = GLOBAL.get('math.affine_118')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 9 + 3)

def test_math_affine_119():
    fn = GLOBAL.get('math.affine_119')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 10 + -3)

def test_math_affine_120():
    fn = GLOBAL.get('math.affine_120')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 11 + -2)

def test_math_affine_121():
    fn = GLOBAL.get('math.affine_121')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 1 + -1)

def test_math_affine_122():
    fn = GLOBAL.get('math.affine_122')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 2 + 0)

def test_math_affine_123():
    fn = GLOBAL.get('math.affine_123')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 3 + 1)

def test_math_affine_124():
    fn = GLOBAL.get('math.affine_124')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 4 + 2)

def test_math_affine_125():
    fn = GLOBAL.get('math.affine_125')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 5 + 3)

def test_math_affine_126():
    fn = GLOBAL.get('math.affine_126')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 6 + -3)

def test_math_affine_127():
    fn = GLOBAL.get('math.affine_127')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 7 + -2)

def test_math_affine_128():
    fn = GLOBAL.get('math.affine_128')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 8 + -1)

def test_math_affine_129():
    fn = GLOBAL.get('math.affine_129')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 9 + 0)

def test_math_affine_130():
    fn = GLOBAL.get('math.affine_130')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 10 + 1)

def test_math_affine_131():
    fn = GLOBAL.get('math.affine_131')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 11 + 2)

def test_math_affine_132():
    fn = GLOBAL.get('math.affine_132')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 1 + 3)

def test_math_affine_133():
    fn = GLOBAL.get('math.affine_133')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 2 + -3)

def test_math_affine_134():
    fn = GLOBAL.get('math.affine_134')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 3 + -2)

def test_math_affine_135():
    fn = GLOBAL.get('math.affine_135')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 4 + -1)

def test_math_affine_136():
    fn = GLOBAL.get('math.affine_136')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 5 + 0)

def test_math_affine_137():
    fn = GLOBAL.get('math.affine_137')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 6 + 1)

def test_math_affine_138():
    fn = GLOBAL.get('math.affine_138')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 7 + 2)

def test_math_affine_139():
    fn = GLOBAL.get('math.affine_139')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 8 + 3)

def test_math_affine_140():
    fn = GLOBAL.get('math.affine_140')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 9 + -3)

def test_math_affine_141():
    fn = GLOBAL.get('math.affine_141')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 10 + -2)

def test_math_affine_142():
    fn = GLOBAL.get('math.affine_142')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 11 + -1)

def test_math_affine_143():
    fn = GLOBAL.get('math.affine_143')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 1 + 0)

def test_math_affine_144():
    fn = GLOBAL.get('math.affine_144')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 2 + 1)

def test_math_affine_145():
    fn = GLOBAL.get('math.affine_145')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 3 + 2)

def test_math_affine_146():
    fn = GLOBAL.get('math.affine_146')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 4 + 3)

def test_math_affine_147():
    fn = GLOBAL.get('math.affine_147')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 5 + -3)

def test_math_affine_148():
    fn = GLOBAL.get('math.affine_148')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 6 + -2)

def test_math_affine_149():
    fn = GLOBAL.get('math.affine_149')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 7 + -1)

def test_math_affine_150():
    fn = GLOBAL.get('math.affine_150')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 8 + 0)

def test_math_affine_151():
    fn = GLOBAL.get('math.affine_151')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 9 + 1)

def test_math_affine_152():
    fn = GLOBAL.get('math.affine_152')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 10 + 2)

def test_math_affine_153():
    fn = GLOBAL.get('math.affine_153')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 11 + 3)

def test_math_affine_154():
    fn = GLOBAL.get('math.affine_154')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 1 + -3)

def test_math_affine_155():
    fn = GLOBAL.get('math.affine_155')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 2 + -2)

def test_math_affine_156():
    fn = GLOBAL.get('math.affine_156')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 3 + -1)

def test_math_affine_157():
    fn = GLOBAL.get('math.affine_157')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 4 + 0)

def test_math_affine_158():
    fn = GLOBAL.get('math.affine_158')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 5 + 1)

def test_math_affine_159():
    fn = GLOBAL.get('math.affine_159')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 6 + 2)

def test_math_affine_160():
    fn = GLOBAL.get('math.affine_160')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 7 + 3)

def test_math_affine_161():
    fn = GLOBAL.get('math.affine_161')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 8 + -3)

def test_math_affine_162():
    fn = GLOBAL.get('math.affine_162')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 9 + -2)

def test_math_affine_163():
    fn = GLOBAL.get('math.affine_163')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 10 + -1)

def test_math_affine_164():
    fn = GLOBAL.get('math.affine_164')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 11 + 0)

def test_math_affine_165():
    fn = GLOBAL.get('math.affine_165')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 1 + 1)

def test_math_affine_166():
    fn = GLOBAL.get('math.affine_166')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 2 + 2)

def test_math_affine_167():
    fn = GLOBAL.get('math.affine_167')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 3 + 3)

def test_math_affine_168():
    fn = GLOBAL.get('math.affine_168')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 4 + -3)

def test_math_affine_169():
    fn = GLOBAL.get('math.affine_169')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 5 + -2)

def test_math_affine_170():
    fn = GLOBAL.get('math.affine_170')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 6 + -1)

def test_math_affine_171():
    fn = GLOBAL.get('math.affine_171')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 7 + 0)

def test_math_affine_172():
    fn = GLOBAL.get('math.affine_172')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 8 + 1)

def test_math_affine_173():
    fn = GLOBAL.get('math.affine_173')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 9 + 2)

def test_math_affine_174():
    fn = GLOBAL.get('math.affine_174')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 10 + 3)

def test_math_affine_175():
    fn = GLOBAL.get('math.affine_175')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 11 + -3)

def test_math_affine_176():
    fn = GLOBAL.get('math.affine_176')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 1 + -2)

def test_math_affine_177():
    fn = GLOBAL.get('math.affine_177')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 2 + -1)

def test_math_affine_178():
    fn = GLOBAL.get('math.affine_178')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 3 + 0)

def test_math_affine_179():
    fn = GLOBAL.get('math.affine_179')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 4 + 1)

def test_math_affine_180():
    fn = GLOBAL.get('math.affine_180')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 5 + 2)

def test_math_affine_181():
    fn = GLOBAL.get('math.affine_181')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 6 + 3)

def test_math_affine_182():
    fn = GLOBAL.get('math.affine_182')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 7 + -3)

def test_math_affine_183():
    fn = GLOBAL.get('math.affine_183')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 8 + -2)

def test_math_affine_184():
    fn = GLOBAL.get('math.affine_184')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 9 + -1)

def test_math_affine_185():
    fn = GLOBAL.get('math.affine_185')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 10 + 0)

def test_math_affine_186():
    fn = GLOBAL.get('math.affine_186')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 11 + 1)

def test_math_affine_187():
    fn = GLOBAL.get('math.affine_187')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 1 + 2)

def test_math_affine_188():
    fn = GLOBAL.get('math.affine_188')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 2 + 3)

def test_math_affine_189():
    fn = GLOBAL.get('math.affine_189')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 3 + -3)

def test_math_affine_190():
    fn = GLOBAL.get('math.affine_190')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 4 + -2)

def test_math_affine_191():
    fn = GLOBAL.get('math.affine_191')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 5 + -1)

def test_math_affine_192():
    fn = GLOBAL.get('math.affine_192')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 6 + 0)

def test_math_affine_193():
    fn = GLOBAL.get('math.affine_193')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 7 + 1)

def test_math_affine_194():
    fn = GLOBAL.get('math.affine_194')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 8 + 2)

def test_math_affine_195():
    fn = GLOBAL.get('math.affine_195')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 9 + 3)

def test_math_affine_196():
    fn = GLOBAL.get('math.affine_196')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 10 + -3)

def test_math_affine_197():
    fn = GLOBAL.get('math.affine_197')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 11 + -2)

def test_math_affine_198():
    fn = GLOBAL.get('math.affine_198')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 1 + -1)

def test_math_affine_199():
    fn = GLOBAL.get('math.affine_199')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 2 + 0)

def test_math_affine_200():
    fn = GLOBAL.get('math.affine_200')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 3 + 1)

def test_math_affine_201():
    fn = GLOBAL.get('math.affine_201')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 4 + 2)

def test_math_affine_202():
    fn = GLOBAL.get('math.affine_202')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 5 + 3)

def test_math_affine_203():
    fn = GLOBAL.get('math.affine_203')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 6 + -3)

def test_math_affine_204():
    fn = GLOBAL.get('math.affine_204')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 7 + -2)

def test_math_affine_205():
    fn = GLOBAL.get('math.affine_205')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 8 + -1)

def test_math_affine_206():
    fn = GLOBAL.get('math.affine_206')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 9 + 0)

def test_math_affine_207():
    fn = GLOBAL.get('math.affine_207')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 10 + 1)

def test_math_affine_208():
    fn = GLOBAL.get('math.affine_208')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 11 + 2)

def test_math_affine_209():
    fn = GLOBAL.get('math.affine_209')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 1 + 3)

def test_math_affine_210():
    fn = GLOBAL.get('math.affine_210')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 2 + -3)

def test_math_affine_211():
    fn = GLOBAL.get('math.affine_211')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 3 + -2)

def test_math_affine_212():
    fn = GLOBAL.get('math.affine_212')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 4 + -1)

def test_math_affine_213():
    fn = GLOBAL.get('math.affine_213')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 5 + 0)

def test_math_affine_214():
    fn = GLOBAL.get('math.affine_214')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 6 + 1)

def test_math_affine_215():
    fn = GLOBAL.get('math.affine_215')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 7 + 2)

def test_math_affine_216():
    fn = GLOBAL.get('math.affine_216')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 8 + 3)

def test_math_affine_217():
    fn = GLOBAL.get('math.affine_217')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 9 + -3)

def test_math_affine_218():
    fn = GLOBAL.get('math.affine_218')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 10 + -2)

def test_math_affine_219():
    fn = GLOBAL.get('math.affine_219')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 11 + -1)

def test_math_affine_220():
    fn = GLOBAL.get('math.affine_220')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 1 + 0)

def test_math_affine_221():
    fn = GLOBAL.get('math.affine_221')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 2 + 1)

def test_math_affine_222():
    fn = GLOBAL.get('math.affine_222')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 3 + 2)

def test_math_affine_223():
    fn = GLOBAL.get('math.affine_223')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 4 + 3)

def test_math_affine_224():
    fn = GLOBAL.get('math.affine_224')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 5 + -3)

def test_math_affine_225():
    fn = GLOBAL.get('math.affine_225')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 6 + -2)

def test_math_affine_226():
    fn = GLOBAL.get('math.affine_226')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 7 + -1)

def test_math_affine_227():
    fn = GLOBAL.get('math.affine_227')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 8 + 0)

def test_math_affine_228():
    fn = GLOBAL.get('math.affine_228')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 9 + 1)

def test_math_affine_229():
    fn = GLOBAL.get('math.affine_229')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 10 + 2)

def test_math_affine_230():
    fn = GLOBAL.get('math.affine_230')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 11 + 3)

def test_math_affine_231():
    fn = GLOBAL.get('math.affine_231')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 1 + -3)

def test_math_affine_232():
    fn = GLOBAL.get('math.affine_232')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 2 + -2)

def test_math_affine_233():
    fn = GLOBAL.get('math.affine_233')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 3 + -1)

def test_math_affine_234():
    fn = GLOBAL.get('math.affine_234')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 4 + 0)

def test_math_affine_235():
    fn = GLOBAL.get('math.affine_235')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 5 + 1)

def test_math_affine_236():
    fn = GLOBAL.get('math.affine_236')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 6 + 2)

def test_math_affine_237():
    fn = GLOBAL.get('math.affine_237')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 7 + 3)

def test_math_affine_238():
    fn = GLOBAL.get('math.affine_238')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 8 + -3)

def test_math_affine_239():
    fn = GLOBAL.get('math.affine_239')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 9 + -2)

def test_math_affine_240():
    fn = GLOBAL.get('math.affine_240')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 10 + -1)

def test_math_affine_241():
    fn = GLOBAL.get('math.affine_241')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 11 + 0)

def test_math_affine_242():
    fn = GLOBAL.get('math.affine_242')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 1 + 1)

def test_math_affine_243():
    fn = GLOBAL.get('math.affine_243')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 2 + 2)

def test_math_affine_244():
    fn = GLOBAL.get('math.affine_244')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 3 + 3)

def test_math_affine_245():
    fn = GLOBAL.get('math.affine_245')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 4 + -3)

def test_math_affine_246():
    fn = GLOBAL.get('math.affine_246')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 5 + -2)

def test_math_affine_247():
    fn = GLOBAL.get('math.affine_247')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 6 + -1)

def test_math_affine_248():
    fn = GLOBAL.get('math.affine_248')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 7 + 0)

def test_math_affine_249():
    fn = GLOBAL.get('math.affine_249')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 8 + 1)

def test_math_affine_250():
    fn = GLOBAL.get('math.affine_250')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 9 + 2)

def test_math_affine_251():
    fn = GLOBAL.get('math.affine_251')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 10 + 3)

def test_math_affine_252():
    fn = GLOBAL.get('math.affine_252')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 11 + -3)

def test_math_affine_253():
    fn = GLOBAL.get('math.affine_253')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 1 + -2)

def test_math_affine_254():
    fn = GLOBAL.get('math.affine_254')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 2 + -1)

def test_math_affine_255():
    fn = GLOBAL.get('math.affine_255')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 3 + 0)

def test_math_affine_256():
    fn = GLOBAL.get('math.affine_256')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 4 + 1)

def test_math_affine_257():
    fn = GLOBAL.get('math.affine_257')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 5 + 2)

def test_math_affine_258():
    fn = GLOBAL.get('math.affine_258')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 6 + 3)

def test_math_affine_259():
    fn = GLOBAL.get('math.affine_259')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 7 + -3)

def test_math_affine_260():
    fn = GLOBAL.get('math.affine_260')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 8 + -2)

def test_math_affine_261():
    fn = GLOBAL.get('math.affine_261')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 9 + -1)

def test_math_affine_262():
    fn = GLOBAL.get('math.affine_262')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 10 + 0)

def test_math_affine_263():
    fn = GLOBAL.get('math.affine_263')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 11 + 1)

def test_math_affine_264():
    fn = GLOBAL.get('math.affine_264')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 1 + 2)

def test_math_affine_265():
    fn = GLOBAL.get('math.affine_265')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 2 + 3)

def test_math_affine_266():
    fn = GLOBAL.get('math.affine_266')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 3 + -3)

def test_math_affine_267():
    fn = GLOBAL.get('math.affine_267')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 4 + -2)

def test_math_affine_268():
    fn = GLOBAL.get('math.affine_268')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 5 + -1)

def test_math_affine_269():
    fn = GLOBAL.get('math.affine_269')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 6 + 0)

def test_math_affine_270():
    fn = GLOBAL.get('math.affine_270')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 7 + 1)

def test_math_affine_271():
    fn = GLOBAL.get('math.affine_271')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 8 + 2)

def test_math_affine_272():
    fn = GLOBAL.get('math.affine_272')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 9 + 3)

def test_math_affine_273():
    fn = GLOBAL.get('math.affine_273')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 10 + -3)

def test_math_affine_274():
    fn = GLOBAL.get('math.affine_274')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 11 + -2)

def test_math_affine_275():
    fn = GLOBAL.get('math.affine_275')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 1 + -1)

def test_math_affine_276():
    fn = GLOBAL.get('math.affine_276')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 2 + 0)

def test_math_affine_277():
    fn = GLOBAL.get('math.affine_277')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 3 + 1)

def test_math_affine_278():
    fn = GLOBAL.get('math.affine_278')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 4 + 2)

def test_math_affine_279():
    fn = GLOBAL.get('math.affine_279')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 5 + 3)

def test_math_affine_280():
    fn = GLOBAL.get('math.affine_280')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 6 + -3)

def test_math_affine_281():
    fn = GLOBAL.get('math.affine_281')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 7 + -2)

def test_math_affine_282():
    fn = GLOBAL.get('math.affine_282')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 8 + -1)

def test_math_affine_283():
    fn = GLOBAL.get('math.affine_283')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 9 + 0)

def test_math_affine_284():
    fn = GLOBAL.get('math.affine_284')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 10 + 1)

def test_math_affine_285():
    fn = GLOBAL.get('math.affine_285')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 11 + 2)

def test_math_affine_286():
    fn = GLOBAL.get('math.affine_286')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 1 + 3)

def test_math_affine_287():
    fn = GLOBAL.get('math.affine_287')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 2 + -3)

def test_math_affine_288():
    fn = GLOBAL.get('math.affine_288')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 3 + -2)

def test_math_affine_289():
    fn = GLOBAL.get('math.affine_289')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 4 + -1)

def test_math_affine_290():
    fn = GLOBAL.get('math.affine_290')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 5 + 0)

def test_math_affine_291():
    fn = GLOBAL.get('math.affine_291')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 6 + 1)

def test_math_affine_292():
    fn = GLOBAL.get('math.affine_292')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 7 + 2)

def test_math_affine_293():
    fn = GLOBAL.get('math.affine_293')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 8 + 3)

def test_math_affine_294():
    fn = GLOBAL.get('math.affine_294')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 9 + -3)

def test_math_affine_295():
    fn = GLOBAL.get('math.affine_295')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 10 + -2)

def test_math_affine_296():
    fn = GLOBAL.get('math.affine_296')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 11 + -1)

def test_math_affine_297():
    fn = GLOBAL.get('math.affine_297')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 1 + 0)

def test_math_affine_298():
    fn = GLOBAL.get('math.affine_298')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 2 + 1)

def test_math_affine_299():
    fn = GLOBAL.get('math.affine_299')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 3 + 2)

def test_math_affine_300():
    fn = GLOBAL.get('math.affine_300')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 4 + 3)

def test_math_affine_301():
    fn = GLOBAL.get('math.affine_301')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 5 + -3)

def test_math_affine_302():
    fn = GLOBAL.get('math.affine_302')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 6 + -2)

def test_math_affine_303():
    fn = GLOBAL.get('math.affine_303')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 7 + -1)

def test_math_affine_304():
    fn = GLOBAL.get('math.affine_304')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 8 + 0)

def test_math_affine_305():
    fn = GLOBAL.get('math.affine_305')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 9 + 1)

def test_math_affine_306():
    fn = GLOBAL.get('math.affine_306')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 10 + 2)

def test_math_affine_307():
    fn = GLOBAL.get('math.affine_307')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 11 + 3)

def test_math_affine_308():
    fn = GLOBAL.get('math.affine_308')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 1 + -3)

def test_math_affine_309():
    fn = GLOBAL.get('math.affine_309')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 2 + -2)

def test_math_affine_310():
    fn = GLOBAL.get('math.affine_310')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 3 + -1)

def test_math_affine_311():
    fn = GLOBAL.get('math.affine_311')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 4 + 0)

def test_math_affine_312():
    fn = GLOBAL.get('math.affine_312')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 5 + 1)

def test_math_affine_313():
    fn = GLOBAL.get('math.affine_313')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 6 + 2)

def test_math_affine_314():
    fn = GLOBAL.get('math.affine_314')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 7 + 3)

def test_math_affine_315():
    fn = GLOBAL.get('math.affine_315')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 8 + -3)

def test_math_affine_316():
    fn = GLOBAL.get('math.affine_316')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 9 + -2)

def test_math_affine_317():
    fn = GLOBAL.get('math.affine_317')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 10 + -1)

def test_math_affine_318():
    fn = GLOBAL.get('math.affine_318')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 11 + 0)

def test_math_affine_319():
    fn = GLOBAL.get('math.affine_319')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 1 + 1)

def test_math_affine_320():
    fn = GLOBAL.get('math.affine_320')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 2 + 2)

def test_math_affine_321():
    fn = GLOBAL.get('math.affine_321')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 3 + 3)

def test_math_affine_322():
    fn = GLOBAL.get('math.affine_322')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 4 + -3)

def test_math_affine_323():
    fn = GLOBAL.get('math.affine_323')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 5 + -2)

def test_math_affine_324():
    fn = GLOBAL.get('math.affine_324')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 6 + -1)

def test_math_affine_325():
    fn = GLOBAL.get('math.affine_325')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 7 + 0)

def test_math_affine_326():
    fn = GLOBAL.get('math.affine_326')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 8 + 1)

def test_math_affine_327():
    fn = GLOBAL.get('math.affine_327')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 9 + 2)

def test_math_affine_328():
    fn = GLOBAL.get('math.affine_328')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 10 + 3)

def test_math_affine_329():
    fn = GLOBAL.get('math.affine_329')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 11 + -3)

def test_math_affine_330():
    fn = GLOBAL.get('math.affine_330')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 1 + -2)

def test_math_affine_331():
    fn = GLOBAL.get('math.affine_331')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 2 + -1)

def test_math_affine_332():
    fn = GLOBAL.get('math.affine_332')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 3 + 0)

def test_math_affine_333():
    fn = GLOBAL.get('math.affine_333')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 4 + 1)

def test_math_affine_334():
    fn = GLOBAL.get('math.affine_334')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 5 + 2)

def test_math_affine_335():
    fn = GLOBAL.get('math.affine_335')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 6 + 3)

def test_math_affine_336():
    fn = GLOBAL.get('math.affine_336')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 7 + -3)

def test_math_affine_337():
    fn = GLOBAL.get('math.affine_337')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 8 + -2)

def test_math_affine_338():
    fn = GLOBAL.get('math.affine_338')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 9 + -1)

def test_math_affine_339():
    fn = GLOBAL.get('math.affine_339')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 10 + 0)

def test_math_affine_340():
    fn = GLOBAL.get('math.affine_340')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 11 + 1)

def test_math_affine_341():
    fn = GLOBAL.get('math.affine_341')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 1 + 2)

def test_math_affine_342():
    fn = GLOBAL.get('math.affine_342')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 2 + 3)

def test_math_affine_343():
    fn = GLOBAL.get('math.affine_343')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 3 + -3)

def test_math_affine_344():
    fn = GLOBAL.get('math.affine_344')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 4 + -2)

def test_math_affine_345():
    fn = GLOBAL.get('math.affine_345')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 5 + -1)

def test_math_affine_346():
    fn = GLOBAL.get('math.affine_346')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 6 + 0)

def test_math_affine_347():
    fn = GLOBAL.get('math.affine_347')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 7 + 1)

def test_math_affine_348():
    fn = GLOBAL.get('math.affine_348')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 8 + 2)

def test_math_affine_349():
    fn = GLOBAL.get('math.affine_349')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 9 + 3)

def test_math_affine_350():
    fn = GLOBAL.get('math.affine_350')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 10 + -3)

def test_math_affine_351():
    fn = GLOBAL.get('math.affine_351')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 11 + -2)

def test_math_affine_352():
    fn = GLOBAL.get('math.affine_352')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 1 + -1)

def test_math_affine_353():
    fn = GLOBAL.get('math.affine_353')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 2 + 0)

def test_math_affine_354():
    fn = GLOBAL.get('math.affine_354')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 3 + 1)

def test_math_affine_355():
    fn = GLOBAL.get('math.affine_355')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 4 + 2)

def test_math_affine_356():
    fn = GLOBAL.get('math.affine_356')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 5 + 3)

def test_math_affine_357():
    fn = GLOBAL.get('math.affine_357')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 6 + -3)

def test_math_affine_358():
    fn = GLOBAL.get('math.affine_358')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 7 + -2)

def test_math_affine_359():
    fn = GLOBAL.get('math.affine_359')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 8 + -1)

def test_math_affine_360():
    fn = GLOBAL.get('math.affine_360')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 9 + 0)

def test_math_affine_361():
    fn = GLOBAL.get('math.affine_361')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 10 + 1)

def test_math_affine_362():
    fn = GLOBAL.get('math.affine_362')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 11 + 2)

def test_math_affine_363():
    fn = GLOBAL.get('math.affine_363')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 1 + 3)

def test_math_affine_364():
    fn = GLOBAL.get('math.affine_364')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 2 + -3)

def test_math_affine_365():
    fn = GLOBAL.get('math.affine_365')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 3 + -2)

def test_math_affine_366():
    fn = GLOBAL.get('math.affine_366')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 4 + -1)

def test_math_affine_367():
    fn = GLOBAL.get('math.affine_367')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 5 + 0)

def test_math_affine_368():
    fn = GLOBAL.get('math.affine_368')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 6 + 1)

def test_math_affine_369():
    fn = GLOBAL.get('math.affine_369')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 7 + 2)

def test_math_affine_370():
    fn = GLOBAL.get('math.affine_370')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 8 + 3)

def test_math_affine_371():
    fn = GLOBAL.get('math.affine_371')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 9 + -3)

def test_math_affine_372():
    fn = GLOBAL.get('math.affine_372')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 10 + -2)

def test_math_affine_373():
    fn = GLOBAL.get('math.affine_373')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 11 + -1)

def test_math_affine_374():
    fn = GLOBAL.get('math.affine_374')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 1 + 0)

def test_math_affine_375():
    fn = GLOBAL.get('math.affine_375')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 2 + 1)

def test_math_affine_376():
    fn = GLOBAL.get('math.affine_376')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 3 + 2)

def test_math_affine_377():
    fn = GLOBAL.get('math.affine_377')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 4 + 3)

def test_math_affine_378():
    fn = GLOBAL.get('math.affine_378')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 5 + -3)

def test_math_affine_379():
    fn = GLOBAL.get('math.affine_379')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 6 + -2)

def test_math_affine_380():
    fn = GLOBAL.get('math.affine_380')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 7 + -1)

def test_math_affine_381():
    fn = GLOBAL.get('math.affine_381')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 8 + 0)

def test_math_affine_382():
    fn = GLOBAL.get('math.affine_382')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 9 + 1)

def test_math_affine_383():
    fn = GLOBAL.get('math.affine_383')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 10 + 2)

def test_math_affine_384():
    fn = GLOBAL.get('math.affine_384')
    assert fn(left=2, right=3, scale=1) == (2 * 11 + 3 * 11 + 3)

def test_math_affine_385():
    fn = GLOBAL.get('math.affine_385')
    assert fn(left=2, right=3, scale=1) == (2 * 12 + 3 * 1 + -3)

def test_math_affine_386():
    fn = GLOBAL.get('math.affine_386')
    assert fn(left=2, right=3, scale=1) == (2 * 13 + 3 * 2 + -2)

def test_math_affine_387():
    fn = GLOBAL.get('math.affine_387')
    assert fn(left=2, right=3, scale=1) == (2 * 14 + 3 * 3 + -1)

def test_math_affine_388():
    fn = GLOBAL.get('math.affine_388')
    assert fn(left=2, right=3, scale=1) == (2 * 15 + 3 * 4 + 0)

def test_math_affine_389():
    fn = GLOBAL.get('math.affine_389')
    assert fn(left=2, right=3, scale=1) == (2 * 16 + 3 * 5 + 1)

def test_math_affine_390():
    fn = GLOBAL.get('math.affine_390')
    assert fn(left=2, right=3, scale=1) == (2 * 17 + 3 * 6 + 2)

def test_math_affine_391():
    fn = GLOBAL.get('math.affine_391')
    assert fn(left=2, right=3, scale=1) == (2 * 1 + 3 * 7 + 3)

def test_math_affine_392():
    fn = GLOBAL.get('math.affine_392')
    assert fn(left=2, right=3, scale=1) == (2 * 2 + 3 * 8 + -3)

def test_math_affine_393():
    fn = GLOBAL.get('math.affine_393')
    assert fn(left=2, right=3, scale=1) == (2 * 3 + 3 * 9 + -2)

def test_math_affine_394():
    fn = GLOBAL.get('math.affine_394')
    assert fn(left=2, right=3, scale=1) == (2 * 4 + 3 * 10 + -1)

def test_math_affine_395():
    fn = GLOBAL.get('math.affine_395')
    assert fn(left=2, right=3, scale=1) == (2 * 5 + 3 * 11 + 0)

def test_math_affine_396():
    fn = GLOBAL.get('math.affine_396')
    assert fn(left=2, right=3, scale=1) == (2 * 6 + 3 * 1 + 1)

def test_math_affine_397():
    fn = GLOBAL.get('math.affine_397')
    assert fn(left=2, right=3, scale=1) == (2 * 7 + 3 * 2 + 2)

def test_math_affine_398():
    fn = GLOBAL.get('math.affine_398')
    assert fn(left=2, right=3, scale=1) == (2 * 8 + 3 * 3 + 3)

def test_math_affine_399():
    fn = GLOBAL.get('math.affine_399')
    assert fn(left=2, right=3, scale=1) == (2 * 9 + 3 * 4 + -3)

def test_math_affine_400():
    fn = GLOBAL.get('math.affine_400')
    assert fn(left=2, right=3, scale=1) == (2 * 10 + 3 * 5 + -2)

def test_text_tag_001():
    out = GLOBAL.get('text.tag_001')(message='x', times=1)
    assert out.startswith('p001:')
    assert out.endswith(':s001')

def test_text_tag_002():
    out = GLOBAL.get('text.tag_002')(message='x', times=1)
    assert out.startswith('p002:')
    assert out.endswith(':s002')

def test_text_tag_003():
    out = GLOBAL.get('text.tag_003')(message='x', times=1)
    assert out.startswith('p003:')
    assert out.endswith(':s003')

def test_text_tag_004():
    out = GLOBAL.get('text.tag_004')(message='x', times=1)
    assert out.startswith('p004:')
    assert out.endswith(':s004')

def test_text_tag_005():
    out = GLOBAL.get('text.tag_005')(message='x', times=1)
    assert out.startswith('p005:')
    assert out.endswith(':s005')

def test_text_tag_006():
    out = GLOBAL.get('text.tag_006')(message='x', times=1)
    assert out.startswith('p006:')
    assert out.endswith(':s006')

def test_text_tag_007():
    out = GLOBAL.get('text.tag_007')(message='x', times=1)
    assert out.startswith('p007:')
    assert out.endswith(':s007')

def test_text_tag_008():
    out = GLOBAL.get('text.tag_008')(message='x', times=1)
    assert out.startswith('p008:')
    assert out.endswith(':s008')

def test_text_tag_009():
    out = GLOBAL.get('text.tag_009')(message='x', times=1)
    assert out.startswith('p009:')
    assert out.endswith(':s009')

def test_text_tag_010():
    out = GLOBAL.get('text.tag_010')(message='x', times=1)
    assert out.startswith('p010:')
    assert out.endswith(':s010')

def test_text_tag_011():
    out = GLOBAL.get('text.tag_011')(message='x', times=1)
    assert out.startswith('p011:')
    assert out.endswith(':s011')

def test_text_tag_012():
    out = GLOBAL.get('text.tag_012')(message='x', times=1)
    assert out.startswith('p012:')
    assert out.endswith(':s012')

def test_text_tag_013():
    out = GLOBAL.get('text.tag_013')(message='x', times=1)
    assert out.startswith('p013:')
    assert out.endswith(':s013')

def test_text_tag_014():
    out = GLOBAL.get('text.tag_014')(message='x', times=1)
    assert out.startswith('p014:')
    assert out.endswith(':s014')

def test_text_tag_015():
    out = GLOBAL.get('text.tag_015')(message='x', times=1)
    assert out.startswith('p015:')
    assert out.endswith(':s015')

def test_text_tag_016():
    out = GLOBAL.get('text.tag_016')(message='x', times=1)
    assert out.startswith('p016:')
    assert out.endswith(':s016')

def test_text_tag_017():
    out = GLOBAL.get('text.tag_017')(message='x', times=1)
    assert out.startswith('p017:')
    assert out.endswith(':s017')

def test_text_tag_018():
    out = GLOBAL.get('text.tag_018')(message='x', times=1)
    assert out.startswith('p018:')
    assert out.endswith(':s018')

def test_text_tag_019():
    out = GLOBAL.get('text.tag_019')(message='x', times=1)
    assert out.startswith('p019:')
    assert out.endswith(':s019')

def test_text_tag_020():
    out = GLOBAL.get('text.tag_020')(message='x', times=1)
    assert out.startswith('p020:')
    assert out.endswith(':s020')

def test_text_tag_021():
    out = GLOBAL.get('text.tag_021')(message='x', times=1)
    assert out.startswith('p021:')
    assert out.endswith(':s021')

def test_text_tag_022():
    out = GLOBAL.get('text.tag_022')(message='x', times=1)
    assert out.startswith('p022:')
    assert out.endswith(':s022')

def test_text_tag_023():
    out = GLOBAL.get('text.tag_023')(message='x', times=1)
    assert out.startswith('p023:')
    assert out.endswith(':s023')

def test_text_tag_024():
    out = GLOBAL.get('text.tag_024')(message='x', times=1)
    assert out.startswith('p024:')
    assert out.endswith(':s024')

def test_text_tag_025():
    out = GLOBAL.get('text.tag_025')(message='x', times=1)
    assert out.startswith('p025:')
    assert out.endswith(':s025')

def test_text_tag_026():
    out = GLOBAL.get('text.tag_026')(message='x', times=1)
    assert out.startswith('p026:')
    assert out.endswith(':s026')

def test_text_tag_027():
    out = GLOBAL.get('text.tag_027')(message='x', times=1)
    assert out.startswith('p027:')
    assert out.endswith(':s027')

def test_text_tag_028():
    out = GLOBAL.get('text.tag_028')(message='x', times=1)
    assert out.startswith('p028:')
    assert out.endswith(':s028')

def test_text_tag_029():
    out = GLOBAL.get('text.tag_029')(message='x', times=1)
    assert out.startswith('p029:')
    assert out.endswith(':s029')

def test_text_tag_030():
    out = GLOBAL.get('text.tag_030')(message='x', times=1)
    assert out.startswith('p030:')
    assert out.endswith(':s030')

def test_text_tag_031():
    out = GLOBAL.get('text.tag_031')(message='x', times=1)
    assert out.startswith('p031:')
    assert out.endswith(':s031')

def test_text_tag_032():
    out = GLOBAL.get('text.tag_032')(message='x', times=1)
    assert out.startswith('p032:')
    assert out.endswith(':s032')

def test_text_tag_033():
    out = GLOBAL.get('text.tag_033')(message='x', times=1)
    assert out.startswith('p033:')
    assert out.endswith(':s033')

def test_text_tag_034():
    out = GLOBAL.get('text.tag_034')(message='x', times=1)
    assert out.startswith('p034:')
    assert out.endswith(':s034')

def test_text_tag_035():
    out = GLOBAL.get('text.tag_035')(message='x', times=1)
    assert out.startswith('p035:')
    assert out.endswith(':s035')

def test_text_tag_036():
    out = GLOBAL.get('text.tag_036')(message='x', times=1)
    assert out.startswith('p036:')
    assert out.endswith(':s036')

def test_text_tag_037():
    out = GLOBAL.get('text.tag_037')(message='x', times=1)
    assert out.startswith('p037:')
    assert out.endswith(':s037')

def test_text_tag_038():
    out = GLOBAL.get('text.tag_038')(message='x', times=1)
    assert out.startswith('p038:')
    assert out.endswith(':s038')

def test_text_tag_039():
    out = GLOBAL.get('text.tag_039')(message='x', times=1)
    assert out.startswith('p039:')
    assert out.endswith(':s039')

def test_text_tag_040():
    out = GLOBAL.get('text.tag_040')(message='x', times=1)
    assert out.startswith('p040:')
    assert out.endswith(':s040')

def test_text_tag_041():
    out = GLOBAL.get('text.tag_041')(message='x', times=1)
    assert out.startswith('p041:')
    assert out.endswith(':s041')

def test_text_tag_042():
    out = GLOBAL.get('text.tag_042')(message='x', times=1)
    assert out.startswith('p042:')
    assert out.endswith(':s042')

def test_text_tag_043():
    out = GLOBAL.get('text.tag_043')(message='x', times=1)
    assert out.startswith('p043:')
    assert out.endswith(':s043')

def test_text_tag_044():
    out = GLOBAL.get('text.tag_044')(message='x', times=1)
    assert out.startswith('p044:')
    assert out.endswith(':s044')

def test_text_tag_045():
    out = GLOBAL.get('text.tag_045')(message='x', times=1)
    assert out.startswith('p045:')
    assert out.endswith(':s045')

def test_text_tag_046():
    out = GLOBAL.get('text.tag_046')(message='x', times=1)
    assert out.startswith('p046:')
    assert out.endswith(':s046')

def test_text_tag_047():
    out = GLOBAL.get('text.tag_047')(message='x', times=1)
    assert out.startswith('p047:')
    assert out.endswith(':s047')

def test_text_tag_048():
    out = GLOBAL.get('text.tag_048')(message='x', times=1)
    assert out.startswith('p048:')
    assert out.endswith(':s048')

def test_text_tag_049():
    out = GLOBAL.get('text.tag_049')(message='x', times=1)
    assert out.startswith('p049:')
    assert out.endswith(':s049')

def test_text_tag_050():
    out = GLOBAL.get('text.tag_050')(message='x', times=1)
    assert out.startswith('p050:')
    assert out.endswith(':s050')

def test_text_tag_051():
    out = GLOBAL.get('text.tag_051')(message='x', times=1)
    assert out.startswith('p051:')
    assert out.endswith(':s051')

def test_text_tag_052():
    out = GLOBAL.get('text.tag_052')(message='x', times=1)
    assert out.startswith('p052:')
    assert out.endswith(':s052')

def test_text_tag_053():
    out = GLOBAL.get('text.tag_053')(message='x', times=1)
    assert out.startswith('p053:')
    assert out.endswith(':s053')

def test_text_tag_054():
    out = GLOBAL.get('text.tag_054')(message='x', times=1)
    assert out.startswith('p054:')
    assert out.endswith(':s054')

def test_text_tag_055():
    out = GLOBAL.get('text.tag_055')(message='x', times=1)
    assert out.startswith('p055:')
    assert out.endswith(':s055')

def test_text_tag_056():
    out = GLOBAL.get('text.tag_056')(message='x', times=1)
    assert out.startswith('p056:')
    assert out.endswith(':s056')

def test_text_tag_057():
    out = GLOBAL.get('text.tag_057')(message='x', times=1)
    assert out.startswith('p057:')
    assert out.endswith(':s057')

def test_text_tag_058():
    out = GLOBAL.get('text.tag_058')(message='x', times=1)
    assert out.startswith('p058:')
    assert out.endswith(':s058')

def test_text_tag_059():
    out = GLOBAL.get('text.tag_059')(message='x', times=1)
    assert out.startswith('p059:')
    assert out.endswith(':s059')

def test_text_tag_060():
    out = GLOBAL.get('text.tag_060')(message='x', times=1)
    assert out.startswith('p060:')
    assert out.endswith(':s060')

def test_text_tag_061():
    out = GLOBAL.get('text.tag_061')(message='x', times=1)
    assert out.startswith('p061:')
    assert out.endswith(':s061')

def test_text_tag_062():
    out = GLOBAL.get('text.tag_062')(message='x', times=1)
    assert out.startswith('p062:')
    assert out.endswith(':s062')

def test_text_tag_063():
    out = GLOBAL.get('text.tag_063')(message='x', times=1)
    assert out.startswith('p063:')
    assert out.endswith(':s063')

def test_text_tag_064():
    out = GLOBAL.get('text.tag_064')(message='x', times=1)
    assert out.startswith('p064:')
    assert out.endswith(':s064')

def test_text_tag_065():
    out = GLOBAL.get('text.tag_065')(message='x', times=1)
    assert out.startswith('p065:')
    assert out.endswith(':s065')

def test_text_tag_066():
    out = GLOBAL.get('text.tag_066')(message='x', times=1)
    assert out.startswith('p066:')
    assert out.endswith(':s066')

def test_text_tag_067():
    out = GLOBAL.get('text.tag_067')(message='x', times=1)
    assert out.startswith('p067:')
    assert out.endswith(':s067')

def test_text_tag_068():
    out = GLOBAL.get('text.tag_068')(message='x', times=1)
    assert out.startswith('p068:')
    assert out.endswith(':s068')

def test_text_tag_069():
    out = GLOBAL.get('text.tag_069')(message='x', times=1)
    assert out.startswith('p069:')
    assert out.endswith(':s069')

def test_text_tag_070():
    out = GLOBAL.get('text.tag_070')(message='x', times=1)
    assert out.startswith('p070:')
    assert out.endswith(':s070')

def test_text_tag_071():
    out = GLOBAL.get('text.tag_071')(message='x', times=1)
    assert out.startswith('p071:')
    assert out.endswith(':s071')

def test_text_tag_072():
    out = GLOBAL.get('text.tag_072')(message='x', times=1)
    assert out.startswith('p072:')
    assert out.endswith(':s072')

def test_text_tag_073():
    out = GLOBAL.get('text.tag_073')(message='x', times=1)
    assert out.startswith('p073:')
    assert out.endswith(':s073')

def test_text_tag_074():
    out = GLOBAL.get('text.tag_074')(message='x', times=1)
    assert out.startswith('p074:')
    assert out.endswith(':s074')

def test_text_tag_075():
    out = GLOBAL.get('text.tag_075')(message='x', times=1)
    assert out.startswith('p075:')
    assert out.endswith(':s075')

def test_text_tag_076():
    out = GLOBAL.get('text.tag_076')(message='x', times=1)
    assert out.startswith('p076:')
    assert out.endswith(':s076')

def test_text_tag_077():
    out = GLOBAL.get('text.tag_077')(message='x', times=1)
    assert out.startswith('p077:')
    assert out.endswith(':s077')

def test_text_tag_078():
    out = GLOBAL.get('text.tag_078')(message='x', times=1)
    assert out.startswith('p078:')
    assert out.endswith(':s078')

def test_text_tag_079():
    out = GLOBAL.get('text.tag_079')(message='x', times=1)
    assert out.startswith('p079:')
    assert out.endswith(':s079')

def test_text_tag_080():
    out = GLOBAL.get('text.tag_080')(message='x', times=1)
    assert out.startswith('p080:')
    assert out.endswith(':s080')

def test_text_tag_081():
    out = GLOBAL.get('text.tag_081')(message='x', times=1)
    assert out.startswith('p081:')
    assert out.endswith(':s081')

def test_text_tag_082():
    out = GLOBAL.get('text.tag_082')(message='x', times=1)
    assert out.startswith('p082:')
    assert out.endswith(':s082')

def test_text_tag_083():
    out = GLOBAL.get('text.tag_083')(message='x', times=1)
    assert out.startswith('p083:')
    assert out.endswith(':s083')

def test_text_tag_084():
    out = GLOBAL.get('text.tag_084')(message='x', times=1)
    assert out.startswith('p084:')
    assert out.endswith(':s084')

def test_text_tag_085():
    out = GLOBAL.get('text.tag_085')(message='x', times=1)
    assert out.startswith('p085:')
    assert out.endswith(':s085')

def test_text_tag_086():
    out = GLOBAL.get('text.tag_086')(message='x', times=1)
    assert out.startswith('p086:')
    assert out.endswith(':s086')

def test_text_tag_087():
    out = GLOBAL.get('text.tag_087')(message='x', times=1)
    assert out.startswith('p087:')
    assert out.endswith(':s087')

def test_text_tag_088():
    out = GLOBAL.get('text.tag_088')(message='x', times=1)
    assert out.startswith('p088:')
    assert out.endswith(':s088')

def test_text_tag_089():
    out = GLOBAL.get('text.tag_089')(message='x', times=1)
    assert out.startswith('p089:')
    assert out.endswith(':s089')

def test_text_tag_090():
    out = GLOBAL.get('text.tag_090')(message='x', times=1)
    assert out.startswith('p090:')
    assert out.endswith(':s090')

def test_text_tag_091():
    out = GLOBAL.get('text.tag_091')(message='x', times=1)
    assert out.startswith('p091:')
    assert out.endswith(':s091')

def test_text_tag_092():
    out = GLOBAL.get('text.tag_092')(message='x', times=1)
    assert out.startswith('p092:')
    assert out.endswith(':s092')

def test_text_tag_093():
    out = GLOBAL.get('text.tag_093')(message='x', times=1)
    assert out.startswith('p093:')
    assert out.endswith(':s093')

def test_text_tag_094():
    out = GLOBAL.get('text.tag_094')(message='x', times=1)
    assert out.startswith('p094:')
    assert out.endswith(':s094')

def test_text_tag_095():
    out = GLOBAL.get('text.tag_095')(message='x', times=1)
    assert out.startswith('p095:')
    assert out.endswith(':s095')

def test_text_tag_096():
    out = GLOBAL.get('text.tag_096')(message='x', times=1)
    assert out.startswith('p096:')
    assert out.endswith(':s096')

def test_text_tag_097():
    out = GLOBAL.get('text.tag_097')(message='x', times=1)
    assert out.startswith('p097:')
    assert out.endswith(':s097')

def test_text_tag_098():
    out = GLOBAL.get('text.tag_098')(message='x', times=1)
    assert out.startswith('p098:')
    assert out.endswith(':s098')

def test_text_tag_099():
    out = GLOBAL.get('text.tag_099')(message='x', times=1)
    assert out.startswith('p099:')
    assert out.endswith(':s099')

def test_text_tag_100():
    out = GLOBAL.get('text.tag_100')(message='x', times=1)
    assert out.startswith('p100:')
    assert out.endswith(':s100')

def test_text_tag_101():
    out = GLOBAL.get('text.tag_101')(message='x', times=1)
    assert out.startswith('p101:')
    assert out.endswith(':s101')

def test_text_tag_102():
    out = GLOBAL.get('text.tag_102')(message='x', times=1)
    assert out.startswith('p102:')
    assert out.endswith(':s102')

def test_text_tag_103():
    out = GLOBAL.get('text.tag_103')(message='x', times=1)
    assert out.startswith('p103:')
    assert out.endswith(':s103')

def test_text_tag_104():
    out = GLOBAL.get('text.tag_104')(message='x', times=1)
    assert out.startswith('p104:')
    assert out.endswith(':s104')

def test_text_tag_105():
    out = GLOBAL.get('text.tag_105')(message='x', times=1)
    assert out.startswith('p105:')
    assert out.endswith(':s105')

def test_text_tag_106():
    out = GLOBAL.get('text.tag_106')(message='x', times=1)
    assert out.startswith('p106:')
    assert out.endswith(':s106')

def test_text_tag_107():
    out = GLOBAL.get('text.tag_107')(message='x', times=1)
    assert out.startswith('p107:')
    assert out.endswith(':s107')

def test_text_tag_108():
    out = GLOBAL.get('text.tag_108')(message='x', times=1)
    assert out.startswith('p108:')
    assert out.endswith(':s108')

def test_text_tag_109():
    out = GLOBAL.get('text.tag_109')(message='x', times=1)
    assert out.startswith('p109:')
    assert out.endswith(':s109')

def test_text_tag_110():
    out = GLOBAL.get('text.tag_110')(message='x', times=1)
    assert out.startswith('p110:')
    assert out.endswith(':s110')

def test_text_tag_111():
    out = GLOBAL.get('text.tag_111')(message='x', times=1)
    assert out.startswith('p111:')
    assert out.endswith(':s111')

def test_text_tag_112():
    out = GLOBAL.get('text.tag_112')(message='x', times=1)
    assert out.startswith('p112:')
    assert out.endswith(':s112')

def test_text_tag_113():
    out = GLOBAL.get('text.tag_113')(message='x', times=1)
    assert out.startswith('p113:')
    assert out.endswith(':s113')

def test_text_tag_114():
    out = GLOBAL.get('text.tag_114')(message='x', times=1)
    assert out.startswith('p114:')
    assert out.endswith(':s114')

def test_text_tag_115():
    out = GLOBAL.get('text.tag_115')(message='x', times=1)
    assert out.startswith('p115:')
    assert out.endswith(':s115')

def test_text_tag_116():
    out = GLOBAL.get('text.tag_116')(message='x', times=1)
    assert out.startswith('p116:')
    assert out.endswith(':s116')

def test_text_tag_117():
    out = GLOBAL.get('text.tag_117')(message='x', times=1)
    assert out.startswith('p117:')
    assert out.endswith(':s117')

def test_text_tag_118():
    out = GLOBAL.get('text.tag_118')(message='x', times=1)
    assert out.startswith('p118:')
    assert out.endswith(':s118')

def test_text_tag_119():
    out = GLOBAL.get('text.tag_119')(message='x', times=1)
    assert out.startswith('p119:')
    assert out.endswith(':s119')

def test_text_tag_120():
    out = GLOBAL.get('text.tag_120')(message='x', times=1)
    assert out.startswith('p120:')
    assert out.endswith(':s120')

def test_text_tag_121():
    out = GLOBAL.get('text.tag_121')(message='x', times=1)
    assert out.startswith('p121:')
    assert out.endswith(':s121')

def test_text_tag_122():
    out = GLOBAL.get('text.tag_122')(message='x', times=1)
    assert out.startswith('p122:')
    assert out.endswith(':s122')

def test_text_tag_123():
    out = GLOBAL.get('text.tag_123')(message='x', times=1)
    assert out.startswith('p123:')
    assert out.endswith(':s123')

def test_text_tag_124():
    out = GLOBAL.get('text.tag_124')(message='x', times=1)
    assert out.startswith('p124:')
    assert out.endswith(':s124')

def test_text_tag_125():
    out = GLOBAL.get('text.tag_125')(message='x', times=1)
    assert out.startswith('p125:')
    assert out.endswith(':s125')

def test_text_tag_126():
    out = GLOBAL.get('text.tag_126')(message='x', times=1)
    assert out.startswith('p126:')
    assert out.endswith(':s126')

def test_text_tag_127():
    out = GLOBAL.get('text.tag_127')(message='x', times=1)
    assert out.startswith('p127:')
    assert out.endswith(':s127')

def test_text_tag_128():
    out = GLOBAL.get('text.tag_128')(message='x', times=1)
    assert out.startswith('p128:')
    assert out.endswith(':s128')

def test_text_tag_129():
    out = GLOBAL.get('text.tag_129')(message='x', times=1)
    assert out.startswith('p129:')
    assert out.endswith(':s129')

def test_text_tag_130():
    out = GLOBAL.get('text.tag_130')(message='x', times=1)
    assert out.startswith('p130:')
    assert out.endswith(':s130')

def test_text_tag_131():
    out = GLOBAL.get('text.tag_131')(message='x', times=1)
    assert out.startswith('p131:')
    assert out.endswith(':s131')

def test_text_tag_132():
    out = GLOBAL.get('text.tag_132')(message='x', times=1)
    assert out.startswith('p132:')
    assert out.endswith(':s132')

def test_text_tag_133():
    out = GLOBAL.get('text.tag_133')(message='x', times=1)
    assert out.startswith('p133:')
    assert out.endswith(':s133')

def test_text_tag_134():
    out = GLOBAL.get('text.tag_134')(message='x', times=1)
    assert out.startswith('p134:')
    assert out.endswith(':s134')

def test_text_tag_135():
    out = GLOBAL.get('text.tag_135')(message='x', times=1)
    assert out.startswith('p135:')
    assert out.endswith(':s135')

def test_text_tag_136():
    out = GLOBAL.get('text.tag_136')(message='x', times=1)
    assert out.startswith('p136:')
    assert out.endswith(':s136')

def test_text_tag_137():
    out = GLOBAL.get('text.tag_137')(message='x', times=1)
    assert out.startswith('p137:')
    assert out.endswith(':s137')

def test_text_tag_138():
    out = GLOBAL.get('text.tag_138')(message='x', times=1)
    assert out.startswith('p138:')
    assert out.endswith(':s138')

def test_text_tag_139():
    out = GLOBAL.get('text.tag_139')(message='x', times=1)
    assert out.startswith('p139:')
    assert out.endswith(':s139')

def test_text_tag_140():
    out = GLOBAL.get('text.tag_140')(message='x', times=1)
    assert out.startswith('p140:')
    assert out.endswith(':s140')

def test_text_tag_141():
    out = GLOBAL.get('text.tag_141')(message='x', times=1)
    assert out.startswith('p141:')
    assert out.endswith(':s141')

def test_text_tag_142():
    out = GLOBAL.get('text.tag_142')(message='x', times=1)
    assert out.startswith('p142:')
    assert out.endswith(':s142')

def test_text_tag_143():
    out = GLOBAL.get('text.tag_143')(message='x', times=1)
    assert out.startswith('p143:')
    assert out.endswith(':s143')

def test_text_tag_144():
    out = GLOBAL.get('text.tag_144')(message='x', times=1)
    assert out.startswith('p144:')
    assert out.endswith(':s144')

def test_text_tag_145():
    out = GLOBAL.get('text.tag_145')(message='x', times=1)
    assert out.startswith('p145:')
    assert out.endswith(':s145')

def test_text_tag_146():
    out = GLOBAL.get('text.tag_146')(message='x', times=1)
    assert out.startswith('p146:')
    assert out.endswith(':s146')

def test_text_tag_147():
    out = GLOBAL.get('text.tag_147')(message='x', times=1)
    assert out.startswith('p147:')
    assert out.endswith(':s147')

def test_text_tag_148():
    out = GLOBAL.get('text.tag_148')(message='x', times=1)
    assert out.startswith('p148:')
    assert out.endswith(':s148')

def test_text_tag_149():
    out = GLOBAL.get('text.tag_149')(message='x', times=1)
    assert out.startswith('p149:')
    assert out.endswith(':s149')

def test_text_tag_150():
    out = GLOBAL.get('text.tag_150')(message='x', times=1)
    assert out.startswith('p150:')
    assert out.endswith(':s150')

def test_text_tag_151():
    out = GLOBAL.get('text.tag_151')(message='x', times=1)
    assert out.startswith('p151:')
    assert out.endswith(':s151')

def test_text_tag_152():
    out = GLOBAL.get('text.tag_152')(message='x', times=1)
    assert out.startswith('p152:')
    assert out.endswith(':s152')

def test_text_tag_153():
    out = GLOBAL.get('text.tag_153')(message='x', times=1)
    assert out.startswith('p153:')
    assert out.endswith(':s153')

def test_text_tag_154():
    out = GLOBAL.get('text.tag_154')(message='x', times=1)
    assert out.startswith('p154:')
    assert out.endswith(':s154')

def test_text_tag_155():
    out = GLOBAL.get('text.tag_155')(message='x', times=1)
    assert out.startswith('p155:')
    assert out.endswith(':s155')

def test_text_tag_156():
    out = GLOBAL.get('text.tag_156')(message='x', times=1)
    assert out.startswith('p156:')
    assert out.endswith(':s156')

def test_text_tag_157():
    out = GLOBAL.get('text.tag_157')(message='x', times=1)
    assert out.startswith('p157:')
    assert out.endswith(':s157')

def test_text_tag_158():
    out = GLOBAL.get('text.tag_158')(message='x', times=1)
    assert out.startswith('p158:')
    assert out.endswith(':s158')

def test_text_tag_159():
    out = GLOBAL.get('text.tag_159')(message='x', times=1)
    assert out.startswith('p159:')
    assert out.endswith(':s159')

def test_text_tag_160():
    out = GLOBAL.get('text.tag_160')(message='x', times=1)
    assert out.startswith('p160:')
    assert out.endswith(':s160')

def test_text_tag_161():
    out = GLOBAL.get('text.tag_161')(message='x', times=1)
    assert out.startswith('p161:')
    assert out.endswith(':s161')

def test_text_tag_162():
    out = GLOBAL.get('text.tag_162')(message='x', times=1)
    assert out.startswith('p162:')
    assert out.endswith(':s162')

def test_text_tag_163():
    out = GLOBAL.get('text.tag_163')(message='x', times=1)
    assert out.startswith('p163:')
    assert out.endswith(':s163')

def test_text_tag_164():
    out = GLOBAL.get('text.tag_164')(message='x', times=1)
    assert out.startswith('p164:')
    assert out.endswith(':s164')

def test_text_tag_165():
    out = GLOBAL.get('text.tag_165')(message='x', times=1)
    assert out.startswith('p165:')
    assert out.endswith(':s165')

def test_text_tag_166():
    out = GLOBAL.get('text.tag_166')(message='x', times=1)
    assert out.startswith('p166:')
    assert out.endswith(':s166')

def test_text_tag_167():
    out = GLOBAL.get('text.tag_167')(message='x', times=1)
    assert out.startswith('p167:')
    assert out.endswith(':s167')

def test_text_tag_168():
    out = GLOBAL.get('text.tag_168')(message='x', times=1)
    assert out.startswith('p168:')
    assert out.endswith(':s168')

def test_text_tag_169():
    out = GLOBAL.get('text.tag_169')(message='x', times=1)
    assert out.startswith('p169:')
    assert out.endswith(':s169')

def test_text_tag_170():
    out = GLOBAL.get('text.tag_170')(message='x', times=1)
    assert out.startswith('p170:')
    assert out.endswith(':s170')

def test_text_tag_171():
    out = GLOBAL.get('text.tag_171')(message='x', times=1)
    assert out.startswith('p171:')
    assert out.endswith(':s171')

def test_text_tag_172():
    out = GLOBAL.get('text.tag_172')(message='x', times=1)
    assert out.startswith('p172:')
    assert out.endswith(':s172')

def test_text_tag_173():
    out = GLOBAL.get('text.tag_173')(message='x', times=1)
    assert out.startswith('p173:')
    assert out.endswith(':s173')

def test_text_tag_174():
    out = GLOBAL.get('text.tag_174')(message='x', times=1)
    assert out.startswith('p174:')
    assert out.endswith(':s174')

def test_text_tag_175():
    out = GLOBAL.get('text.tag_175')(message='x', times=1)
    assert out.startswith('p175:')
    assert out.endswith(':s175')

def test_text_tag_176():
    out = GLOBAL.get('text.tag_176')(message='x', times=1)
    assert out.startswith('p176:')
    assert out.endswith(':s176')

def test_text_tag_177():
    out = GLOBAL.get('text.tag_177')(message='x', times=1)
    assert out.startswith('p177:')
    assert out.endswith(':s177')

def test_text_tag_178():
    out = GLOBAL.get('text.tag_178')(message='x', times=1)
    assert out.startswith('p178:')
    assert out.endswith(':s178')

def test_text_tag_179():
    out = GLOBAL.get('text.tag_179')(message='x', times=1)
    assert out.startswith('p179:')
    assert out.endswith(':s179')

def test_text_tag_180():
    out = GLOBAL.get('text.tag_180')(message='x', times=1)
    assert out.startswith('p180:')
    assert out.endswith(':s180')

def test_text_tag_181():
    out = GLOBAL.get('text.tag_181')(message='x', times=1)
    assert out.startswith('p181:')
    assert out.endswith(':s181')

def test_text_tag_182():
    out = GLOBAL.get('text.tag_182')(message='x', times=1)
    assert out.startswith('p182:')
    assert out.endswith(':s182')

def test_text_tag_183():
    out = GLOBAL.get('text.tag_183')(message='x', times=1)
    assert out.startswith('p183:')
    assert out.endswith(':s183')

def test_text_tag_184():
    out = GLOBAL.get('text.tag_184')(message='x', times=1)
    assert out.startswith('p184:')
    assert out.endswith(':s184')

def test_text_tag_185():
    out = GLOBAL.get('text.tag_185')(message='x', times=1)
    assert out.startswith('p185:')
    assert out.endswith(':s185')

def test_text_tag_186():
    out = GLOBAL.get('text.tag_186')(message='x', times=1)
    assert out.startswith('p186:')
    assert out.endswith(':s186')

def test_text_tag_187():
    out = GLOBAL.get('text.tag_187')(message='x', times=1)
    assert out.startswith('p187:')
    assert out.endswith(':s187')

def test_text_tag_188():
    out = GLOBAL.get('text.tag_188')(message='x', times=1)
    assert out.startswith('p188:')
    assert out.endswith(':s188')

def test_text_tag_189():
    out = GLOBAL.get('text.tag_189')(message='x', times=1)
    assert out.startswith('p189:')
    assert out.endswith(':s189')

def test_text_tag_190():
    out = GLOBAL.get('text.tag_190')(message='x', times=1)
    assert out.startswith('p190:')
    assert out.endswith(':s190')

def test_text_tag_191():
    out = GLOBAL.get('text.tag_191')(message='x', times=1)
    assert out.startswith('p191:')
    assert out.endswith(':s191')

def test_text_tag_192():
    out = GLOBAL.get('text.tag_192')(message='x', times=1)
    assert out.startswith('p192:')
    assert out.endswith(':s192')

def test_text_tag_193():
    out = GLOBAL.get('text.tag_193')(message='x', times=1)
    assert out.startswith('p193:')
    assert out.endswith(':s193')

def test_text_tag_194():
    out = GLOBAL.get('text.tag_194')(message='x', times=1)
    assert out.startswith('p194:')
    assert out.endswith(':s194')

def test_text_tag_195():
    out = GLOBAL.get('text.tag_195')(message='x', times=1)
    assert out.startswith('p195:')
    assert out.endswith(':s195')

def test_text_tag_196():
    out = GLOBAL.get('text.tag_196')(message='x', times=1)
    assert out.startswith('p196:')
    assert out.endswith(':s196')

def test_text_tag_197():
    out = GLOBAL.get('text.tag_197')(message='x', times=1)
    assert out.startswith('p197:')
    assert out.endswith(':s197')

def test_text_tag_198():
    out = GLOBAL.get('text.tag_198')(message='x', times=1)
    assert out.startswith('p198:')
    assert out.endswith(':s198')

def test_text_tag_199():
    out = GLOBAL.get('text.tag_199')(message='x', times=1)
    assert out.startswith('p199:')
    assert out.endswith(':s199')

def test_text_tag_200():
    out = GLOBAL.get('text.tag_200')(message='x', times=1)
    assert out.startswith('p200:')
    assert out.endswith(':s200')

def test_seq_fold_001():
    out = GLOBAL.get('seq.fold_001')(items=[1, 2])
    assert out == float(2) + 3.0

def test_seq_fold_002():
    out = GLOBAL.get('seq.fold_002')(items=[1, 2])
    assert out == float(5) + 3.0

def test_seq_fold_003():
    out = GLOBAL.get('seq.fold_003')(items=[1, 2])
    assert out == float(8) + 3.0

def test_seq_fold_004():
    out = GLOBAL.get('seq.fold_004')(items=[1, 2])
    assert out == float(11) + 3.0

def test_seq_fold_005():
    out = GLOBAL.get('seq.fold_005')(items=[1, 2])
    assert out == float(14) + 3.0

def test_seq_fold_006():
    out = GLOBAL.get('seq.fold_006')(items=[1, 2])
    assert out == float(17) + 3.0

def test_seq_fold_007():
    out = GLOBAL.get('seq.fold_007')(items=[1, 2])
    assert out == float(20) + 3.0

def test_seq_fold_008():
    out = GLOBAL.get('seq.fold_008')(items=[1, 2])
    assert out == float(23) + 3.0

def test_seq_fold_009():
    out = GLOBAL.get('seq.fold_009')(items=[1, 2])
    assert out == float(26) + 3.0

def test_seq_fold_010():
    out = GLOBAL.get('seq.fold_010')(items=[1, 2])
    assert out == float(29) + 3.0

def test_seq_fold_011():
    out = GLOBAL.get('seq.fold_011')(items=[1, 2])
    assert out == float(32) + 3.0

def test_seq_fold_012():
    out = GLOBAL.get('seq.fold_012')(items=[1, 2])
    assert out == float(35) + 3.0

def test_seq_fold_013():
    out = GLOBAL.get('seq.fold_013')(items=[1, 2])
    assert out == float(38) + 3.0

def test_seq_fold_014():
    out = GLOBAL.get('seq.fold_014')(items=[1, 2])
    assert out == float(41) + 3.0

def test_seq_fold_015():
    out = GLOBAL.get('seq.fold_015')(items=[1, 2])
    assert out == float(44) + 3.0

def test_seq_fold_016():
    out = GLOBAL.get('seq.fold_016')(items=[1, 2])
    assert out == float(47) + 3.0

def test_seq_fold_017():
    out = GLOBAL.get('seq.fold_017')(items=[1, 2])
    assert out == float(50) + 3.0

def test_seq_fold_018():
    out = GLOBAL.get('seq.fold_018')(items=[1, 2])
    assert out == float(53) + 3.0

def test_seq_fold_019():
    out = GLOBAL.get('seq.fold_019')(items=[1, 2])
    assert out == float(56) + 3.0

def test_seq_fold_020():
    out = GLOBAL.get('seq.fold_020')(items=[1, 2])
    assert out == float(59) + 3.0

def test_seq_fold_021():
    out = GLOBAL.get('seq.fold_021')(items=[1, 2])
    assert out == float(62) + 3.0

def test_seq_fold_022():
    out = GLOBAL.get('seq.fold_022')(items=[1, 2])
    assert out == float(65) + 3.0

def test_seq_fold_023():
    out = GLOBAL.get('seq.fold_023')(items=[1, 2])
    assert out == float(68) + 3.0

def test_seq_fold_024():
    out = GLOBAL.get('seq.fold_024')(items=[1, 2])
    assert out == float(71) + 3.0

def test_seq_fold_025():
    out = GLOBAL.get('seq.fold_025')(items=[1, 2])
    assert out == float(74) + 3.0

def test_seq_fold_026():
    out = GLOBAL.get('seq.fold_026')(items=[1, 2])
    assert out == float(77) + 3.0

def test_seq_fold_027():
    out = GLOBAL.get('seq.fold_027')(items=[1, 2])
    assert out == float(80) + 3.0

def test_seq_fold_028():
    out = GLOBAL.get('seq.fold_028')(items=[1, 2])
    assert out == float(83) + 3.0

def test_seq_fold_029():
    out = GLOBAL.get('seq.fold_029')(items=[1, 2])
    assert out == float(86) + 3.0

def test_seq_fold_030():
    out = GLOBAL.get('seq.fold_030')(items=[1, 2])
    assert out == float(89) + 3.0

def test_seq_fold_031():
    out = GLOBAL.get('seq.fold_031')(items=[1, 2])
    assert out == float(92) + 3.0

def test_seq_fold_032():
    out = GLOBAL.get('seq.fold_032')(items=[1, 2])
    assert out == float(95) + 3.0

def test_seq_fold_033():
    out = GLOBAL.get('seq.fold_033')(items=[1, 2])
    assert out == float(98) + 3.0

def test_seq_fold_034():
    out = GLOBAL.get('seq.fold_034')(items=[1, 2])
    assert out == float(101) + 3.0

def test_seq_fold_035():
    out = GLOBAL.get('seq.fold_035')(items=[1, 2])
    assert out == float(104) + 3.0

def test_seq_fold_036():
    out = GLOBAL.get('seq.fold_036')(items=[1, 2])
    assert out == float(107) + 3.0

def test_seq_fold_037():
    out = GLOBAL.get('seq.fold_037')(items=[1, 2])
    assert out == float(110) + 3.0

def test_seq_fold_038():
    out = GLOBAL.get('seq.fold_038')(items=[1, 2])
    assert out == float(113) + 3.0

def test_seq_fold_039():
    out = GLOBAL.get('seq.fold_039')(items=[1, 2])
    assert out == float(116) + 3.0

def test_seq_fold_040():
    out = GLOBAL.get('seq.fold_040')(items=[1, 2])
    assert out == float(119) + 3.0

def test_seq_fold_041():
    out = GLOBAL.get('seq.fold_041')(items=[1, 2])
    assert out == float(122) + 3.0

def test_seq_fold_042():
    out = GLOBAL.get('seq.fold_042')(items=[1, 2])
    assert out == float(125) + 3.0

def test_seq_fold_043():
    out = GLOBAL.get('seq.fold_043')(items=[1, 2])
    assert out == float(128) + 3.0

def test_seq_fold_044():
    out = GLOBAL.get('seq.fold_044')(items=[1, 2])
    assert out == float(131) + 3.0

def test_seq_fold_045():
    out = GLOBAL.get('seq.fold_045')(items=[1, 2])
    assert out == float(134) + 3.0

def test_seq_fold_046():
    out = GLOBAL.get('seq.fold_046')(items=[1, 2])
    assert out == float(137) + 3.0

def test_seq_fold_047():
    out = GLOBAL.get('seq.fold_047')(items=[1, 2])
    assert out == float(140) + 3.0

def test_seq_fold_048():
    out = GLOBAL.get('seq.fold_048')(items=[1, 2])
    assert out == float(143) + 3.0

def test_seq_fold_049():
    out = GLOBAL.get('seq.fold_049')(items=[1, 2])
    assert out == float(146) + 3.0

def test_seq_fold_050():
    out = GLOBAL.get('seq.fold_050')(items=[1, 2])
    assert out == float(149) + 3.0

def test_seq_fold_051():
    out = GLOBAL.get('seq.fold_051')(items=[1, 2])
    assert out == float(152) + 3.0

def test_seq_fold_052():
    out = GLOBAL.get('seq.fold_052')(items=[1, 2])
    assert out == float(155) + 3.0

def test_seq_fold_053():
    out = GLOBAL.get('seq.fold_053')(items=[1, 2])
    assert out == float(158) + 3.0

def test_seq_fold_054():
    out = GLOBAL.get('seq.fold_054')(items=[1, 2])
    assert out == float(161) + 3.0

def test_seq_fold_055():
    out = GLOBAL.get('seq.fold_055')(items=[1, 2])
    assert out == float(164) + 3.0

def test_seq_fold_056():
    out = GLOBAL.get('seq.fold_056')(items=[1, 2])
    assert out == float(167) + 3.0

def test_seq_fold_057():
    out = GLOBAL.get('seq.fold_057')(items=[1, 2])
    assert out == float(170) + 3.0

def test_seq_fold_058():
    out = GLOBAL.get('seq.fold_058')(items=[1, 2])
    assert out == float(173) + 3.0

def test_seq_fold_059():
    out = GLOBAL.get('seq.fold_059')(items=[1, 2])
    assert out == float(176) + 3.0

def test_seq_fold_060():
    out = GLOBAL.get('seq.fold_060')(items=[1, 2])
    assert out == float(179) + 3.0

def test_seq_fold_061():
    out = GLOBAL.get('seq.fold_061')(items=[1, 2])
    assert out == float(182) + 3.0

def test_seq_fold_062():
    out = GLOBAL.get('seq.fold_062')(items=[1, 2])
    assert out == float(185) + 3.0

def test_seq_fold_063():
    out = GLOBAL.get('seq.fold_063')(items=[1, 2])
    assert out == float(188) + 3.0

def test_seq_fold_064():
    out = GLOBAL.get('seq.fold_064')(items=[1, 2])
    assert out == float(191) + 3.0

def test_seq_fold_065():
    out = GLOBAL.get('seq.fold_065')(items=[1, 2])
    assert out == float(194) + 3.0

def test_seq_fold_066():
    out = GLOBAL.get('seq.fold_066')(items=[1, 2])
    assert out == float(197) + 3.0

def test_seq_fold_067():
    out = GLOBAL.get('seq.fold_067')(items=[1, 2])
    assert out == float(200) + 3.0

def test_seq_fold_068():
    out = GLOBAL.get('seq.fold_068')(items=[1, 2])
    assert out == float(203) + 3.0

def test_seq_fold_069():
    out = GLOBAL.get('seq.fold_069')(items=[1, 2])
    assert out == float(206) + 3.0

def test_seq_fold_070():
    out = GLOBAL.get('seq.fold_070')(items=[1, 2])
    assert out == float(209) + 3.0

def test_seq_fold_071():
    out = GLOBAL.get('seq.fold_071')(items=[1, 2])
    assert out == float(212) + 3.0

def test_seq_fold_072():
    out = GLOBAL.get('seq.fold_072')(items=[1, 2])
    assert out == float(215) + 3.0

def test_seq_fold_073():
    out = GLOBAL.get('seq.fold_073')(items=[1, 2])
    assert out == float(218) + 3.0

def test_seq_fold_074():
    out = GLOBAL.get('seq.fold_074')(items=[1, 2])
    assert out == float(221) + 3.0

def test_seq_fold_075():
    out = GLOBAL.get('seq.fold_075')(items=[1, 2])
    assert out == float(224) + 3.0

def test_seq_fold_076():
    out = GLOBAL.get('seq.fold_076')(items=[1, 2])
    assert out == float(227) + 3.0

def test_seq_fold_077():
    out = GLOBAL.get('seq.fold_077')(items=[1, 2])
    assert out == float(230) + 3.0

def test_seq_fold_078():
    out = GLOBAL.get('seq.fold_078')(items=[1, 2])
    assert out == float(233) + 3.0

def test_seq_fold_079():
    out = GLOBAL.get('seq.fold_079')(items=[1, 2])
    assert out == float(236) + 3.0

def test_seq_fold_080():
    out = GLOBAL.get('seq.fold_080')(items=[1, 2])
    assert out == float(239) + 3.0

def test_seq_fold_081():
    out = GLOBAL.get('seq.fold_081')(items=[1, 2])
    assert out == float(242) + 3.0

def test_seq_fold_082():
    out = GLOBAL.get('seq.fold_082')(items=[1, 2])
    assert out == float(245) + 3.0

def test_seq_fold_083():
    out = GLOBAL.get('seq.fold_083')(items=[1, 2])
    assert out == float(248) + 3.0

def test_seq_fold_084():
    out = GLOBAL.get('seq.fold_084')(items=[1, 2])
    assert out == float(251) + 3.0

def test_seq_fold_085():
    out = GLOBAL.get('seq.fold_085')(items=[1, 2])
    assert out == float(254) + 3.0

def test_seq_fold_086():
    out = GLOBAL.get('seq.fold_086')(items=[1, 2])
    assert out == float(257) + 3.0

def test_seq_fold_087():
    out = GLOBAL.get('seq.fold_087')(items=[1, 2])
    assert out == float(260) + 3.0

def test_seq_fold_088():
    out = GLOBAL.get('seq.fold_088')(items=[1, 2])
    assert out == float(263) + 3.0

def test_seq_fold_089():
    out = GLOBAL.get('seq.fold_089')(items=[1, 2])
    assert out == float(266) + 3.0

def test_seq_fold_090():
    out = GLOBAL.get('seq.fold_090')(items=[1, 2])
    assert out == float(269) + 3.0

def test_seq_fold_091():
    out = GLOBAL.get('seq.fold_091')(items=[1, 2])
    assert out == float(272) + 3.0

def test_seq_fold_092():
    out = GLOBAL.get('seq.fold_092')(items=[1, 2])
    assert out == float(275) + 3.0

def test_seq_fold_093():
    out = GLOBAL.get('seq.fold_093')(items=[1, 2])
    assert out == float(278) + 3.0

def test_seq_fold_094():
    out = GLOBAL.get('seq.fold_094')(items=[1, 2])
    assert out == float(281) + 3.0

def test_seq_fold_095():
    out = GLOBAL.get('seq.fold_095')(items=[1, 2])
    assert out == float(284) + 3.0

def test_seq_fold_096():
    out = GLOBAL.get('seq.fold_096')(items=[1, 2])
    assert out == float(287) + 3.0

def test_seq_fold_097():
    out = GLOBAL.get('seq.fold_097')(items=[1, 2])
    assert out == float(290) + 3.0

def test_seq_fold_098():
    out = GLOBAL.get('seq.fold_098')(items=[1, 2])
    assert out == float(293) + 3.0

def test_seq_fold_099():
    out = GLOBAL.get('seq.fold_099')(items=[1, 2])
    assert out == float(296) + 3.0

def test_seq_fold_100():
    out = GLOBAL.get('seq.fold_100')(items=[1, 2])
    assert out == float(299) + 3.0

def test_seq_fold_101():
    out = GLOBAL.get('seq.fold_101')(items=[1, 2])
    assert out == float(302) + 3.0

def test_seq_fold_102():
    out = GLOBAL.get('seq.fold_102')(items=[1, 2])
    assert out == float(305) + 3.0

def test_seq_fold_103():
    out = GLOBAL.get('seq.fold_103')(items=[1, 2])
    assert out == float(308) + 3.0

def test_seq_fold_104():
    out = GLOBAL.get('seq.fold_104')(items=[1, 2])
    assert out == float(311) + 3.0

def test_seq_fold_105():
    out = GLOBAL.get('seq.fold_105')(items=[1, 2])
    assert out == float(314) + 3.0

def test_seq_fold_106():
    out = GLOBAL.get('seq.fold_106')(items=[1, 2])
    assert out == float(317) + 3.0

def test_seq_fold_107():
    out = GLOBAL.get('seq.fold_107')(items=[1, 2])
    assert out == float(320) + 3.0

def test_seq_fold_108():
    out = GLOBAL.get('seq.fold_108')(items=[1, 2])
    assert out == float(323) + 3.0

def test_seq_fold_109():
    out = GLOBAL.get('seq.fold_109')(items=[1, 2])
    assert out == float(326) + 3.0

def test_seq_fold_110():
    out = GLOBAL.get('seq.fold_110')(items=[1, 2])
    assert out == float(329) + 3.0

def test_seq_fold_111():
    out = GLOBAL.get('seq.fold_111')(items=[1, 2])
    assert out == float(332) + 3.0

def test_seq_fold_112():
    out = GLOBAL.get('seq.fold_112')(items=[1, 2])
    assert out == float(335) + 3.0

def test_seq_fold_113():
    out = GLOBAL.get('seq.fold_113')(items=[1, 2])
    assert out == float(338) + 3.0

def test_seq_fold_114():
    out = GLOBAL.get('seq.fold_114')(items=[1, 2])
    assert out == float(341) + 3.0

def test_seq_fold_115():
    out = GLOBAL.get('seq.fold_115')(items=[1, 2])
    assert out == float(344) + 3.0

def test_seq_fold_116():
    out = GLOBAL.get('seq.fold_116')(items=[1, 2])
    assert out == float(347) + 3.0

def test_seq_fold_117():
    out = GLOBAL.get('seq.fold_117')(items=[1, 2])
    assert out == float(350) + 3.0

def test_seq_fold_118():
    out = GLOBAL.get('seq.fold_118')(items=[1, 2])
    assert out == float(353) + 3.0

def test_seq_fold_119():
    out = GLOBAL.get('seq.fold_119')(items=[1, 2])
    assert out == float(356) + 3.0

def test_seq_fold_120():
    out = GLOBAL.get('seq.fold_120')(items=[1, 2])
    assert out == float(359) + 3.0

def test_seq_fold_121():
    out = GLOBAL.get('seq.fold_121')(items=[1, 2])
    assert out == float(362) + 3.0

def test_seq_fold_122():
    out = GLOBAL.get('seq.fold_122')(items=[1, 2])
    assert out == float(365) + 3.0

def test_seq_fold_123():
    out = GLOBAL.get('seq.fold_123')(items=[1, 2])
    assert out == float(368) + 3.0

def test_seq_fold_124():
    out = GLOBAL.get('seq.fold_124')(items=[1, 2])
    assert out == float(371) + 3.0

def test_seq_fold_125():
    out = GLOBAL.get('seq.fold_125')(items=[1, 2])
    assert out == float(374) + 3.0

def test_seq_fold_126():
    out = GLOBAL.get('seq.fold_126')(items=[1, 2])
    assert out == float(377) + 3.0

def test_seq_fold_127():
    out = GLOBAL.get('seq.fold_127')(items=[1, 2])
    assert out == float(380) + 3.0

def test_seq_fold_128():
    out = GLOBAL.get('seq.fold_128')(items=[1, 2])
    assert out == float(383) + 3.0

def test_seq_fold_129():
    out = GLOBAL.get('seq.fold_129')(items=[1, 2])
    assert out == float(386) + 3.0

def test_seq_fold_130():
    out = GLOBAL.get('seq.fold_130')(items=[1, 2])
    assert out == float(389) + 3.0

def test_seq_fold_131():
    out = GLOBAL.get('seq.fold_131')(items=[1, 2])
    assert out == float(392) + 3.0

def test_seq_fold_132():
    out = GLOBAL.get('seq.fold_132')(items=[1, 2])
    assert out == float(395) + 3.0

def test_seq_fold_133():
    out = GLOBAL.get('seq.fold_133')(items=[1, 2])
    assert out == float(398) + 3.0

def test_seq_fold_134():
    out = GLOBAL.get('seq.fold_134')(items=[1, 2])
    assert out == float(401) + 3.0

def test_seq_fold_135():
    out = GLOBAL.get('seq.fold_135')(items=[1, 2])
    assert out == float(404) + 3.0

def test_seq_fold_136():
    out = GLOBAL.get('seq.fold_136')(items=[1, 2])
    assert out == float(407) + 3.0

def test_seq_fold_137():
    out = GLOBAL.get('seq.fold_137')(items=[1, 2])
    assert out == float(410) + 3.0

def test_seq_fold_138():
    out = GLOBAL.get('seq.fold_138')(items=[1, 2])
    assert out == float(413) + 3.0

def test_seq_fold_139():
    out = GLOBAL.get('seq.fold_139')(items=[1, 2])
    assert out == float(416) + 3.0

def test_seq_fold_140():
    out = GLOBAL.get('seq.fold_140')(items=[1, 2])
    assert out == float(419) + 3.0

