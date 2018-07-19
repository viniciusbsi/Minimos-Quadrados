from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__, template_folder='templates')
app = Flask(__name__, static_folder='static')


@app.route("/")
def minimoQuadrados():
    return render_template('index.html')


@app.route('/minimosQuadrados', methods=['POST'])
def init():
    pontosX = request.form['X']
    pontosY = request.form['Y']
    matrizX = []
    matrizY = []
    if(len(pontosX) != len(pontosY)):
        return render_template('index.html', msg="Deve-se ter o mesmo número de pontos para X e Y !")

    else:
        for ponto in pontosX:
            matrizX.append(int(ponto))
        for ponto in pontosY:
            matrizY.append(int(ponto))

        matrizU = defineMatrizU(len(pontosX))
        p = defineP(matrizX, matrizY, matrizU)
        m = defineM(matrizX, matrizY, matrizU)
        return render_template('index.html', m=str(m), p=str(p))


def defineP(matrizX, matrizY, matrizU):

    # DIVIDENDO: (Y^t*U)  =  A #
    YtU = np.dot(matrizY, matrizU)

    # DIVIDENDO (X^t*X)  =  B #
    XtX = np.dot(matrizX, matrizX)

    # DIVIDENDO (Y^t*Y)  =  C #
    YtY = np.dot(matrizY, matrizY)

    # DIVIDENDO (X^t*U)  =  D #
    XtU = np.dot(matrizX, matrizU)

    # DIVIDENDO A*B #
    AB = YtU * XtX

    # DIVIDENDO C*D #
    CD = YtY * XtU

    # DIVIDENDO (AB - CD) #
    AB_sub_CD = AB - CD

    # DIVISOR DA DIVISÃO #

    # DIVISOR (U^t*U) =  E #
    UtU = np.dot(matrizU, matrizU)

    # DIVISOR (X^t*X) MULTIPLICAÇÃO JÁ FEITA NO ITEM B  = F #

    # DIVISOR (X^t*U)² = G #
    XtU_square = XtU * XtU

    # DIVISOR E*F #
    EF = UtU * XtX

    # DIVISOR EF - XtU_square#
    EF_sub_XtU_square = EF - XtU_square

    #  DIVISÃO  #
    final = AB_sub_CD / EF_sub_XtU_square

    print(AB_sub_CD)
    print(EF_sub_XtU_square)
    return (str(final))

def defineM(matrizX, matrizY, matrizU):

    # DIVIDENDO: (Y^t*Y)  =  A #
    YtY = np.dot(matrizY, matrizY)

    # DIVIDENDO (U^t*U)  =  B #
    UtU = np.dot(matrizU, matrizU)

    # DIVIDENDO (Y^t*U)  =  C #
    YtU = np.dot(matrizY, matrizU)

    # DIVIDENDO (X^t*U)  =  D #
    XtU = np.dot(matrizX, matrizU)

    # DIVIDENDO A*B #
    AB = YtY * UtU

    # DIVIDENDO C*D #
    CD = YtU * XtU

    # DIVIDENDO (AB - CD) #
    AB_sub_CD = AB - CD

    # DIVISOR DA DIVISÃO #

    # DIVISOR (U^t*U) =  E #
    UtU = np.dot(matrizU, matrizU)

    # DIVISOR (X^t*X) F #
    XtX = np.dot(matrizX, matrizX)

    # DIVISOR (X^t*U)² = G #
    XtU_square = XtU * XtU

    # DIVISOR E*F #
    EF = UtU * XtX

    # DIVISOR EF - XtU_square#
    EF_sub_XtU_square = EF - XtU_square

    #  DIVISÃO  #
    final = AB_sub_CD / EF_sub_XtU_square

    print(AB_sub_CD)
    print(EF_sub_XtU_square)
    return (str(final))

def defineMatrizU(tamanho):
    i = 0
    u = []
    while (i < tamanho):
        u.append(1)
        i = i + 1
    return u

if __name__ == "__main__":
    app.debug = True
    app.run()
    minimoQuadrados()
