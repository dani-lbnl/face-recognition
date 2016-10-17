print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn import preprocessing

from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from sklearn.datasets import load_svmlight_file
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.datasets import load_svmlight_file
from sklearn.svm import SVC,LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import numpy
import numpy as np
from sklearn import grid_search
import multiprocessing
from sklearn.metrics import classification_report


lb = preprocessing.LabelBinarizer()
#X, y = load_svmlight_file("/home/eucassio/mestrado/face-recognition/gabor/resultados/processados/03072016/teste.txt")

X, y = load_svmlight_file("/media/eucassio/dados/facedatabase/vetores de caracteristicas ARFACE/filtro_gabor_entropia_2pi_ARface_48_56_expressoes_0_100_8_4x4_5x8_15x15__concatenado.txt")
X = X.toarray()
print len(X)
yLabels = range(1,101);




# Binarize the output
lb = preprocessing.LabelBinarizer()
y=lb.fit_transform(y)

#y = label_binarize(y, np.unique(y))
#print y
#n_classes = y.shape[1]

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30,
                                                    random_state=0)

# Learn to predict each class against the other
#classifier = OneVsRestClassifier(svm.SVC(kernel='rbf', gamma=0.000030517578125, C = 8.0,  probability=True))
#classifier = svm.SVC(kernel='rbf', gamma=0.000030517578125, C = 8.0,  probability=True, decision_function_shape='ovr')

cores=multiprocessing.cpu_count()-2


svr = OneVsRestClassifier(LinearSVC(C=0.0001,class_weight='balanced'),n_jobs=cores) ################LinearSVC Code faster        
    #svr = OneVsRestClassifier(SVC(kernel='linear', probability=True,  ##################SVC code slow
    #   class_weight='auto'),n_jobs=cores)


fi2 = svr.fit(X_train, y_train)

y_true, y_pred = y_test, svr.predict(X_test)

predicted = y_pred 

relatorio_classificacao = (classification_report(y_true, y_pred))

y_score = fi2.decision_function(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
#for i in range(n_classes):
#   fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
#    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
#y_test = label_binarize(y_test, np.unique(y_test))
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_pred.ravel())

roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])



precisaomacro = precision_score(y_test, predicted, average='macro')  
precisaomicro = precision_score(y_test, predicted, average='micro')  
precisaoweighted = precision_score(y_test, predicted, average='weighted')  

acuracia = metrics.accuracy_score(y_test, predicted)  
con = confusion_matrix(lb.inverse_transform(y_test), lb.inverse_transform(predicted))

f1Scoremacro = f1_score(y_test, predicted, average='macro')
f1Scoremicro = f1_score(y_test, predicted, average='micro')  
f1Scoreweighted = f1_score(y_test, predicted, average='weighted')  


recallmacro = recall_score(y_test, predicted, average='macro')  
recallmicro = recall_score(y_test, predicted, average='micro')
recallweighted = recall_score(y_test, predicted, average='weighted')

f = open('resultados.txt','wb')

f.write('precisao    macro: ' + '{}'.format(precisaomacro)+'\n')
f.write('precisao    micro: ' + '{}'.format(precisaomicro)+'\n')
f.write('precisao weighted: ' + '{}'.format(precisaoweighted)+'\n\n')

f.write('acuracia: ' + '{}'.format(acuracia)+'\n\n')

f.write('f1Score    macro: ' + '{}'.format(f1Scoremacro)+'\n')
f.write('f1Score    micro: ' + '{}'.format(f1Scoremicro)+'\n')
f.write('f1Score weighted: ' + '{}'.format(f1Scoreweighted)+'\n\n')

f.write('recall    macro: ' + '{}'.format(recallmacro)+'\n')
f.write('recall    micro: ' + '{}'.format(recallmicro)+'\n')
f.write('recall weighted: ' + '{}'.format(recallweighted)+'\n\n')

f.write('AUC            : ' + '{}'.format(roc_auc["micro"])+'\n\n')

numpy.savetxt(f,con,fmt="%s")

f.write(format(relatorio_classificacao)+'\n')

f.close()




plt.figure()
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         linewidth=2)


#for i in range(n_classes):
#    plt.plot(fpr[i], tpr[i], label='ROC curve of class {0} (area = {1:0.2f})'
#                                   ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
#plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.savefig('roc.eps', format='eps', dpi=1000)
