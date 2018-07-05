# Copyright (c) 2009 IW.
# All rights reserved.
#
# Author: liuqw <liuqingwei@chuangxin.com>
# Date:   2018/6/27
# coding=utf-8
"""
"""

from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

'''
读取乳腺癌数据集
数据集前两列存储样本ID和诊断结果（M代表恶性，B代表良性）
3~32列包含了30个特征
'''
df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',
    header=None)
X = df.loc[:, 2:].values
y = df.loc[:, 1].values
le = LabelEncoder()
# 将类标从字符串(M或B)变为整数的(0,1)
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=0)

'''
在流水线中集成标准化操作以及分类器
PipeLine对象采用元组的序列作为输入，每个元组第一个值为字符串，
可以通过字符串访问流水线的元素，第二个值为sklearn中的转换器或评估器
'''
pipe_svc = Pipeline([
    ('scl', StandardScaler()),
    ('clf', SVC(random_state=0))
])

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

# 以字典的方式定义待调优的超参数
param_dist = {'clf__C': param_range,
              'clf__kernel': ['linear', 'rbf'],
              'clf__gamma': param_range}

rs = RandomizedSearchCV(estimator=pipe_svc,
                        param_distributions=param_dist,
                        cv=10)

rs.fit(X_train, y_train)
print(rs.best_score_)
'''
输出最佳k折交叉验证准确率：
0.9802197802197802
'''
print(rs.best_params_)
'''
最优的超参数信息：
{'clf__C': 10.0, 'clf__gamma': 0.01, 'clf__kernel': 'rbf'}
'''
clf = rs.best_estimator_
clf.fit(X_train, y_train)
print('Test accuracy: %.3f' % clf.score(X_test, y_test))
'''
Test accuracy: 0.982
'''
