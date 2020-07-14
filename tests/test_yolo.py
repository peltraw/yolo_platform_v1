import pytest
from yolo.yolo import Yolo

def test_yolo_객체_생성():
	yolo = Yolo()
	assert yolo != None

"""
def test_fit_호출시_model_id_반환():
	yolo = Yolo()
	model_id = yolo.fit()
	assert model_id != None
"""


"""
def test_fit_호출시_async_확인():
def test_fit_호출시_반환되는_model_id가_None이_아닌_지_확인():
def test_fit_호출시_상태파일이_생성되는_지_확인():
def test_fit_호출시_반환되는_model_id가_매번_다른_지_확인():
def test_fit_호출시_이미_학습되고_있으면_예외가_던져지는_지_확인():
def test_fit_호출시_path가_없으면_예외가_던져지는_지_확인():
def test_fit_호출시_path가_정해진_구조가_아니면_예외가_던져지는_지_확인():
def test_fit_호출시_model_id를_주어졌을때_반환된_model_id가_동일한_지_확인():
def test_fit_호출시_model_id가_주어지고_기존_path가_다를때_적용되는지_확인():
"""



