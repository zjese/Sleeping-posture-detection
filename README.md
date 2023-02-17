# Sleeping-posture-detection
**Innovation and Entrepreneurship Training Program for college students in 2019, ZengJin**<br>

## 项目情况
**这是我们团队于2019年立项的大学生创新创业训练计划项目，2021年6月通过结项**<br>
[关于2021年度大学生创新创业训练计划项目校内结题验收结果的公示](https://jwc.gdpu.edu.cn/info/1081/3020.htm)

## 项目内容简介
>对睡姿的长期自动监测是医疗、健康领域中的一项关键技术，在疾病的防治中，睡眠姿势信息也占有十分重要的地位。这套检测系统基于计算机视觉，运用python语言，基于tensorflow及keras框架，实现使用kinect摄像头获取照片，以及对左卧、右卧、正躺、左蜷缩、右蜷缩等共计15种睡眠姿势的分类与检测，模型的识别准确率达到90%以上。通过该项目的实操锻炼，能熟练掌握运用tensorflow及keras解决目标检测、分类、识别问题，并深入理解深度神经网络的构造及原理。

## 团队成员
**曾进 老志辉 许绵渠**

## 数据库说明
>该数据库由普通数据集、深度图数据集、红外图像数据集以及骨骼图数据集共4个数据集组成，为了方便在研究中对比不同数据集的训练效果，要求四个数据集之间的区别仅为图像种类，而拍摄角度，受试者的动作等则应该保持一致。因此，我们在构建数据库时，对参与样本采集者某一时刻做出的同一个动作，我们的采集方案是：同时采集该动作的普通图、深度图、红外图以及骨骼图。比如，数据集中记录正躺姿势的文件夹，其中标号为1的图像，为方便表述，记为正躺1号，则4个数据集中的正躺1号均对应受试者同一时刻的同一动作，区别仅在于图像种类。<br>
<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86%E5%B9%B3%E5%8F%B0.png" width="40%" height="40%"></div>

>**注意：由于数据库图像涉及到团队成员隐私及肖像权问题，此页面仅给出数据库概况，同时给出建立数据库的代码实现，若您有兴趣进行同类研究，可[参考该过程建立自己的数据集。](https://github.com/zjese/Sleeping-posture-detection/tree/master/dataset_building)**

## 样本类型

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%A0%B7%E6%9C%AC%E7%B1%BB%E5%9E%8B.png" width="90%" height="90%"></div>

## 数据集大小

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%95%B0%E6%8D%AE%E9%9B%86%E5%A4%A7%E5%B0%8F%E5%8F%8A%E8%A7%84%E6%A8%A1.png" width="90%" height="90%"></div>

## 普通数据集

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%B6%B5%E7%9B%96%E5%A7%BF%E5%8A%BF_%E6%99%AE%E9%80%9A%E6%95%B0%E6%8D%AE%E9%9B%86.png" width="60%" height="60%"></div>

## 深度图数据集

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%B6%B5%E7%9B%96%E6%A0%B7%E6%9C%AC_%E6%B7%B1%E5%BA%A6%E5%9B%BE%E6%95%B0%E6%8D%AE%E9%9B%86.png" width="60%" height="60%"></div>

## 红外图像数据集

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%B6%B5%E7%9B%96%E6%A0%B7%E6%9C%AC_%E7%BA%A2%E5%A4%96%E6%95%B0%E6%8D%AE%E9%9B%86.png" width="60%" height="60%"></div>

## 骨骼图数据集

<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E6%B6%B5%E7%9B%96%E6%A0%B7%E6%9C%AC_%E9%AA%A8%E9%AA%BC%E5%9B%BE%E6%95%B0%E6%8D%AE%E9%9B%86.png" width="60%" height="60%"></div>

## 训练
在训练中，我们主要使用了VGG，ResNet，DenseNet，InceptionResNet四个系列的模型，用以对比网络深度分别为20，50，120，570时对模型训练的影响，为简化使用，在代码中，我们仅给出[基于迁移学习的VGG16模型代码实现](https://github.com/zjese/Sleeping-posture-detection/blob/master/train_VGG16.ipynb)。

## 损失函数及优化器

<table class="MsoTableGrid" border="1" align="center" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="277" style="width:207.4pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US">loss<o:p></o:p></span></b></p>
  </td>
  <td width="277" style="width:207.4pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US">optimizer<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="277" rowspan="4" style="width:207.4pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">categorical_crossentropy</span></span></p>
  </td>
  <td width="277" style="width:207.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">Adam</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="277" style="width:207.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US">SGD</span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3">
  <td width="277" style="width:207.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">Ftrl</span></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;mso-yfti-lastrow:yes">
  <td width="277" style="width:207.4pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">Nadam</span></span></p>
  </td>
 </tr>
</tbody></table>

## 测试
在实验中，80%的数据用于训练，20%的数据用于测试，这里建议您使用**sklearn**的api接口**train_test_split**对数据集进行划分<br>
```
from sklearn.model_selection import train_test_split
(trainX, testX, trainY, testY) = train_test_split(data, labels,
                                                  test_size=0.20, stratify=labels, random_state=42)
```
<br>
经过整理，给出两个主要实验结果：1.样本质量对模型的影响；2.网络深度对模型的影响。<br>

### 样本质量对模型的影响
<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/4%E7%A7%8D%E6%A0%B7%E6%9C%AC%E5%88%86%E7%B1%BB%E8%AF%AF%E5%B7%AE%E5%AF%B9%E6%AF%94.png" width="40%" height="40%"></div>

### 网络深度对模型的影响
<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E7%BD%91%E7%BB%9C%E6%B7%B1%E5%BA%A6%E4%B8%8E%E8%AF%AF%E5%B7%AE%E5%AF%B9%E6%AF%94.png" width="40%" height="40%"></div>

## 分类特征可视化
<div align=center><img src="https://github.com/zjese/Sleeping-posture-detection/blob/master/img/%E7%BA%A2%E5%A4%96%E5%9B%BE%E5%83%8F%E5%88%86%E7%B1%BB%E7%89%B9%E5%BE%81%E5%8F%AF%E8%A7%86%E5%8C%96.png" width="50%" height="50%"></div>

>选取红外图像样本，并将分类依据可视化标注于图上。
