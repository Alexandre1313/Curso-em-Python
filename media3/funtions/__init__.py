def convert(par1, par2, par3, par4, par5, par6, simu):
    tex = [par1, par2, par3, par4, par5, par6, simu]
    tex1 = []
    try:
        if tex[0] != '':
            tex1.append(str(tex[0].capitalize()))
        else:
            return '', 1, 0.0, 0.0, 0.0, 0.0, 0.0
    except(ValueError, TypeError):
        return '', 1, 0.0, 0.0, 0.0, 0.0, 0.0
    else:
        try:
            if tex[1] != '':
                sm = int(tex[1].strip())
                if 6 >= sm >= 1:
                    tex1.append(sm)
                else:
                    return '##', 7, 0.0, 0.0, 0.0, 0.0, 0.0
            else:
                return '##', 8, 0.0, 0.0, 0.0, 0.0, 0.0
        except(ValueError, TypeError):
            return '##', 7, 0.0, 0.0, 0.0, 0.0, 0.0
        else:
            try:
                if tex[2] != '':
                    n1 = float(tex[2].strip())
                    if 0 <= n1 <= 10:
                        tex1.append(n1)
                    else:
                        return '##', 1, 13.0, 0.0, 0.0, 0.0, 0.0
                else:
                    tex1.append(-1.0)
            except(ValueError, TypeError):
                return '##', 1, 13.0, 0.0, 0.0, 0.0, 0.0
            else:
                try:
                    if tex[3] != '':
                        n2 = float(tex[3].strip())
                        if 0 <= n2 <= 10:
                            tex1.append(n2)
                        else:
                            return '##', 1, 0.0, 13.0, 0.0, 0.0, 0.0
                    else:
                        tex1.append(-1.0)
                except(ValueError, TypeError):
                    return '##', 1, 0.0, 13.0, 0.0, 0.0, 0.0
                else:
                    try:
                        if tex[4] != '':
                            n3 = float(tex[4].strip())
                            if 0 <= n3 <= 10:
                                tex1.append(n3)
                            else:
                                return '##', 1, 0.0, 0.0, 13.0, 0.0, 0.0
                        else:
                            tex1.append(-1.0)
                    except(ValueError, TypeError):
                        return '##', 1, 0.0, 0.0, 13.0, 0.0, 0.0
                    else:
                        try:
                            if tex[5] != '':
                                n4 = float(tex[5].strip())
                                if 0 <= n4 <= 10:
                                    tex1.append(n4)
                                else:
                                    return '##', 1, 0.0, 0.0, 0.0, 13.0, 0.0
                            else:
                                tex1.append(-1.0)
                        except(ValueError, TypeError):
                            return '##', 1, 0.0, 0.0, 0.0, 13.0, 0.0
                        else:
                            try:
                                if tex[6] != '':
                                    sim = float(tex[6].strip())
                                    if 0 <= sim <= 2:
                                        tex1.append(sim)
                                    else:
                                        return '##', 1, 0.0, 0.0, 0.0, 0.0, 13.0
                                else:
                                    tex1.append(-1.0)
                            except(ValueError, TypeError):
                                return '##', 1, 0.0, 0.0, 0.0, 0.0, 13.0
                            else:
                                return tex1[0], tex1[1], tex1[2], tex1[3], tex1[4], tex1[5], tex1[6]


def _should_round_down(val: float):
    if val < 0:
        return ((val * -1) % 1) < 0.5
    return (val % 1) < 0.5


def _round(val: float, ndigits=0):
    import math
    if ndigits > 0:
        val *= 10 ** (ndigits - 1)
    is_positive = val > 0
    tmp_val = val
    if not is_positive:
        tmp_val *= -1
    rounded_value = math.floor(tmp_val) if _should_round_down(val) else math.ceil(tmp_val)
    if not is_positive:
        rounded_value *= -1
    if ndigits > 0:
        rounded_value /= 10 ** (ndigits - 1)
    return rounded_value


class Banco:
    def __init__(self, materia='', semestre=0, nota1=0.0,
                 nota2=0.0, nota3=0.0,
                 nota4=0.0, simu=0.0, calculo=False):
        if materia != '':
            self.mt = materia
        else:
            self.mt = '<vazia>'
            print('ERRO-O campo referente à matéria não pode ser vazio!')
        if 6 >= semestre >= 1:
            self.sm = semestre
        else:
            if semestre == 8:
                self.sm = 8
                print('ERRO-O campo referente ao semestre não pode ser vazio!')
            if semestre == 7:
                self.sm = 7
                print('ERRO-O campo referente ao semestre deve conter um valor "inteiro" entre 1 e 6!')
        if 10 >= nota1 >= 0:
            self.n1 = nota1
        else:
            if nota1 == -1.0:
                self.n1 = nota1
            if nota1 == 13:
                self.n1 = 13
                print('ERRO-O campo referente à avaliação 01 deve conter um valor entre 0 e 10!')
        if 10 >= nota2 >= 0:
            self.n2 = nota2
        else:
            if nota2 == -1.0:
                self.n2 = nota2
            if nota2 == 13:
                self.n2 = 13
                print('ERRO-O campo referente à avaliação 02 deve conter um valor entre 0 e 10!')
        if 10 >= nota3 >= 0:
            self.n3 = nota3
        else:
            if nota3 == -1.0 or nota3 == -2.0:
                self.n3 = nota3
            if nota3 == 13:
                self.n3 = 13
                print('ERRO-O campo referente à avaliação 03 deve conter um valor entre 0 e 10!')
        if 10 >= nota4 >= 0:
            self.n4 = nota4
        else:
            if nota4 == -1.0 or nota4 == -2.0:
                self.n4 = nota4
            if nota4 == 13:
                self.n4 = 13
                print('ERRO-O campo referente à avaliação 04 deve conter um valor entre 0 e 10!')
        if 2 >= simu >= 0:
            self.si = simu
        else:
            if simu == -1.0:
                self.si = simu
            if simu == 13:
                self.si = 13
                print('ERRO-O campo referente ao simulado deve conter um valor entre 0 e 2!')
        if calculo == 'F' or calculo is False:
            calculo = False
            self.calc = calculo
        else:
            if calculo == 'T' or calculo is True:
                calculo = True
                self.calc = calculo

    @staticmethod
    def animation(msg):
        from time import sleep
        print(f'{msg}', end='')
        cont = 56
        while cont > 0:
            print('>', end='')
            cont -= 1
            sleep(0.00000001)

    @staticmethod
    def anime(*args):
        from time import sleep
        janela = args[0]
        chave = args[1]
        simbol = args[2]
        quant1 = args[3]
        quant2 = args[4]
        msg = args[5]
        cont1 = quant1
        while cont1 > 0:
            print(f'{msg} ', end='')
            cont2 = quant2
            cont3 = 1
            while cont2 > 0:
                print(f'{simbol} ', end='')
                cont2 -= 1
                cont3 += 1
                sleep(0.000000000000001)
            cont1 -= 1
            quant2 += 7
            janela.find_element(chave).Update('')

    @staticmethod
    def linhas(msg: str, c: int = 0, b: int = 0, mo: str = 'ne'):
        caract = msg.strip()
        mos = mo
        if mos == 'ne':
            if c == 0:
                ci = len(caract) + 4
            else:
                ci = c
            if b == 0:
                ba = len(caract) + 4
            else:
                ba = b
            print('=' * ci)
            print(f'  {caract}')
            print('=' * ba)
        if mos == 'mc':
            if c == 0:
                ci = len(caract) + 4
            else:
                ci = c
            print('=' * ci)
            print(f'  {caract}')
        if mos == 'mb':
            if b == 0:
                ba = len(caract) + 4
            else:
                ba = b
            print(f'  {caract}')
            print('=' * ba)
        if mos == 'nm':
            print(f'  {caract}')

    @staticmethod
    def criar():
        import sqlite3
        data = sqlite3.connect('data.db')
        c1 = data.cursor()
        data.execute('''CREATE TABLE IF NOT EXISTS data(
                      MATERIA TEXT PRIMARY KEY NOT NULL ,
                      SEMESTRE INTERGER NOT NULL , 
                      NOTA1 REAL NOT NULL ,
                      MD1 REAL NOT NULL ,
                      NOTA2 REAL NOT NULL ,
                      MD2 REAL NOT NULL ,
                      NOTA3 REAL NOT NULL ,
                      MD3 REAL NOT NULL ,
                      NOTA4 REAL NOT NULL ,
                      MD4 REAL NOT NULL ,
                      SIMULADO REAL NOT NULL,
                      MDF REAL NOT NULL ,
                      PDAM REAL NOT NULL ,
                      TIPO TEXT NOT NULL,
                      SITMAT TEXT NOT NULL,
                      SITAL TEXT NOT NULL)''')
        data.commit()
        c1.close()
        data.close()

    @staticmethod
    def escrever(mt, sm, n1, md1, n2, md2, n3, md3, n4, md4, simu, mdf, pdam, tipo, sitmat, sital):
        import sqlite3
        from time import sleep
        temp = 0.01
        cm = bx = 83
        contador = 1
        val = (mt, sm, n1, md1, n2, md2, n3, md3, n4, md4, simu, mdf, pdam, tipo, sitmat, sital)
        if val[0] != '<vazia>':
            if 6 >= val[1] >= 1:
                if (10 >= val[2] >= -2.0 and 10 >= val[4] >= -2.0 and 10 >= val[6] >= -2.0
                        and 10 >= val[8] >= -2.0 and 2 >= val[10] >= -2.0):
                    data1 = sqlite3.connect('data.db')
                    c1 = data1.cursor()
                    try:
                        c1.execute('''INSERT into data(materia, semestre, nota1, md1, nota2,
                         md2, nota3, md3, nota4, md4, simulado, mdf, pdam,
                         tipo, sitmat, sital) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8],
                                    val[9], val[10], val[11], val[12], val[13], val[14], val[15]))
                        data1.commit()
                    except sqlite3.Error as erro:
                        Banco.linhas(f'{erro}', cm, bx, 'ne')
                    else:
                        if val[13] == 'F':
                            Banco.linhas('SUCESSO-Dados gravados com êxito!', cm, bx, 'ne')
                            sleep(temp)
                            print(f'MATÉRIA  ==  {val[0]}')
                            sleep(temp)
                            print(f'SEMESTRE  ==  {val[1]}')
                            sleep(temp)
                            if val[2] != -1.0:
                                print(f'NOTA 01  ==  {val[2]} \nMD1  ==  {val[3]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 01  ==  vazia \nMD1  ==  vazia')
                                sleep(temp)
                            if val[4] != -1.0:
                                print(f'NOTA 02  ==  {val[4]} \nMD2  ==  {val[5]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 02  ==  vazia \nMD2  ==  vazia')
                                sleep(temp)
                            if val[6] != -1.0:
                                print(f'NOTA 03  ==  {val[6]} \nMD3  ==  {val[7]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 03  ==  vazia \nMD3  ==  vazia')
                                sleep(temp)
                            if val[8] != -1.0:
                                print(f'NOTA 04  ==  {val[8]} \nMD4  ==  {val[9]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 04  ==  vazia \nMD4  ==  vazia')
                                sleep(temp)
                            if val[10] != -1.0:
                                print(f'SIMULADO  ==  {val[10]}')
                                sleep(temp)
                            else:
                                print(f'SIMULADO  ==  vazia')
                                sleep(temp)
                            if val[2] != -1.0 and val[4] != -1.0 and val[6] != -1.0 and val[8] != -1.0:
                                print(f'MDF  ==  {val[11]} \nPDAM  ==  {val[12]:.1f}%')
                                sleep(temp)
                            else:
                                print(f'MDF  ==  vazia \nPDAM  ==  vazia')
                                sleep(temp)
                            print(f'TIPO  ==  {val[13]}')
                        else:
                            Banco.linhas('SUCESSO-Dados gravados com êxito!', cm, bx, 'ne')
                            sleep(temp)
                            print(f'MATÉRIA  ==  {val[0]}')
                            sleep(temp)
                            print(f'SEMESTRE  ==  {val[1]}')
                            sleep(temp)
                            if val[2] != -1.0:
                                print(f'NOTA 01  ==  {val[2]} \nMD1  ==  {val[3]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 01  ==  vazia \nMD1  ==  vazia')
                                sleep(temp)
                            if val[4] != -1.0:
                                print(f'NOTA 02  ==  {val[4]} \nMD2  ==  {val[5]}')
                                sleep(temp)
                            else:
                                print(f'NOTA 02  ==  vazia \nMD2  ==  vazia')
                                sleep(temp)
                            if val[10] != -1.0:
                                print(f'SIMULADO  ==  {val[10]}')
                                sleep(temp)
                            else:
                                print(f'SIMULADO  ==  vazia')
                                sleep(temp)
                            if val[2] != -1.0 and val[4] != -1.0:
                                print(f'MDF  ==  {val[11]} \nPDAM  ==  {val[12]:.1f}%')
                                sleep(temp)
                            else:
                                print(f'MDF  ==  vazia \nPDAM  ==  vazia')
                                sleep(temp)
                            print(f'TIPO  ==  {val[13]}')
                    finally:
                        c1.close()
                        data1.close()
        return contador

    def calcular_banco(self):
        if self.mt != '<vazia>' and 1 <= self.sm <= 6:
            if (-2 <= self.n1 <= 10 and -2 <= self.n2 <= 10 and -2 <= self.n3 <= 10 and -2 <= self.n4 <= 10
                    and -2 <= self.si <= 2):
                if self.calc is True:
                    media7 = 7.0
                    media10 = 10.0
                    media6 = 6.51
                    if self.n1 != -1:
                        md1 = self.n1 * 7.00 / 10
                    else:
                        md1 = -1.0
                    if self.n2 != -1.0:
                        md2 = self.n2 * 3.00 / 10
                    else:
                        md2 = -1.0
                    if self.si != -1.0:
                        simul = self.si
                    else:
                        simul = -1.0
                    if md1 != -1.0 and md2 != -1.0:
                        if simul == -1.0:
                            mdf = (md1 + md2)
                            pdam = mdf * 100 / media10
                            if mdf >= media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, -1.0, mdf, pdam, 'T', 'Concluída', 'Aprovado')
                            elif media6 <= mdf < media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, -1.0, mdf, pdam, 'T', 'Concluída', 'Ap. arred.')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, -1.0, mdf, pdam, 'T', 'Concluída', 'Reprovado')
                        else:
                            mdf = (md1 + md2 + simul)
                            if mdf > media10:
                                mdf = media10
                            pdam = mdf * 100 / media10
                            if mdf >= media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, simul, mdf, pdam, 'T', 'Concluída', 'Aprovado')
                            elif media6 <= mdf < media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, simul, mdf, pdam, 'T', 'Concluída', 'Ap. arred.')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, simul, mdf, pdam, 'T', 'Concluída', 'Reprovado')
                    else:
                        if md1 == -1.0 and md2 == -1.0 and simul == -1.0:
                            return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                    -2.0, -2.0, -2.0, -2.0, -1.0, -1.0, -1.0, 'T', 'À cursar', 'Indefinida')
                        else:
                            if simul == -1.0:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, -1.0, -1.0, -1.0, 'T', 'Em curso', 'Cursando')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        -2.0, -2.0, -2.0, -2.0, simul, -1.0, -1.0, 'T', 'Em curso', 'Cursando')
                else:
                    media7 = 7.0
                    media10 = 10.0
                    media6 = 6.51
                    if self.n1 != -1.0:
                        md1 = self.n1 * 1.50 / 10
                    else:
                        md1 = -1.0
                    if self.n2 != -1.0:
                        md2 = self.n2 * 1.50 / 10
                    else:
                        md2 = -1.0
                    if self.n3 != -1.0:
                        md3 = self.n3 * 4.00 / 10
                    else:
                        md3 = -1.0
                    if self.n4 != -1.0:
                        md4 = self.n4 * 3.00 / 10
                    else:
                        md4 = -1.0
                    if self.si != -1.0:
                        simul = self.si
                    else:
                        simul = -1.0
                    if md1 != -1.0 and md2 != -1.0 and md3 != -1.0 and md4 != -1.0:
                        if simul == -1.0:
                            mdf = (md1 + md2 + md3 + md4)
                            pdam = mdf * 100 / media10
                            if mdf >= media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, -1.0, mdf, pdam, 'F', 'Concluída', 'Aprovado')
                            elif media6 <= mdf < media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, -1.0, mdf, pdam, 'F', 'Concluída', 'Ap. arred.')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, -1.0, mdf, pdam, 'F', 'Concluída', 'Reprovado')
                        else:
                            mdf = (md1 + md2 + md3 + md4 + simul)
                            if mdf > media10:
                                mdf = media10
                            pdam = mdf * 100 / media10
                            if mdf >= media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, simul, mdf, pdam, 'F', 'Concluída', 'Aprovado')
                            elif media6 <= mdf < media7:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, simul, mdf, pdam, 'F', 'Concluída', 'Ap. arred.')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, simul, mdf, pdam, 'F', 'Concluída', 'Reprovado')
                    else:
                        if md1 == -1.0 and md2 == -1.0 and md3 == -1.0 and md4 == -1.0 and simul == -1.0:
                            return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                    self.n3, md3, self.n4, md4, -1.0, -1.0, -1.0, 'F', 'À cursar', 'Indefinida')
                        else:
                            if simul == -1.0:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, -1.0, -1.0, -1.0, 'F', 'Em curso', 'Cursando')
                            else:
                                return (self.mt, self.sm, self.n1, md1, self.n2, md2,
                                        self.n3, md3, self.n4, md4, simul, -1.0, -1.0, 'F', 'Em curso', 'Cursando')
            else:
                return '<vazia>', 8, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        else:
            return '<vazia>', 8, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    @staticmethod
    def carr_linha(mat):
        import sqlite3
        data = sqlite3.connect('data.db')
        c1 = data.cursor()
        records = None
        try:
            c1.execute('''SELECT materia, semestre, nota1, nota2, nota3,
                          nota4, simulado, tipo, sitmat, sital from data where materia = ?''', (mat,))
        except sqlite3.Error as erro:
            print(erro)
        else:
            records = c1.fetchall()
        finally:
            c1.close()
            data.close()
        if records:
            valores = list()
            for t in records:
                for ny in t:
                    valores.append(ny)
            return valores
        else:
            return ['', '', '', '', '', '']

    @staticmethod
    def carr_materias():
        import sqlite3
        data = sqlite3.connect('data.db')
        c1 = data.cursor()
        records = None
        try:
            c1.execute('''SELECT materia from data order by semestre''')
        except sqlite3.Error as erro:
            print(erro)
        else:
            records = c1.fetchall()
        finally:
            c1.close()
            data.close()
        if records is not None:
            valores = list()
            for t in records:
                for n in t:
                    valores.append(n)
            return valores
        else:
            return ''

    @staticmethod
    def regrav(n1, md1, n2, md2, n3, md3, n4, md4, sim, mdf, pdam,
               tipo, sitmat, sital, materia, cdn1, cdn2, cdn3, cdn4, cdns, dfn1, dfn2, dfn3, dfn4, dfns):
        reg = (n1, md1, n2, md2, n3, md3, n4, md4, sim, mdf, pdam, tipo, sitmat, sital, materia)
        cond = (cdn1, cdn2, cdn3, cdn4, cdns)
        ig = (dfn1, dfn2, dfn3, dfn4, dfns)
        cm = bx = 83
        if (10 >= reg[0] >= -2.0 and 10 >= reg[2] >= -2.0 and 10 >= reg[4] >= -2.0
                and 10 >= reg[6] >= -2.0 and -2.0 <= reg[8] <= 2):
            import sqlite3
            data = sqlite3.connect('data.db')
            c1 = data.cursor()
            try:
                c1.execute('''UPDATE  data SET nota1 = ?, md1 = ?, nota2 = ?,
                              md2 = ?, nota3 = ?,
                              md3 = ?, nota4 = ?, md4 = ?, simulado = ?,
                              mdf = ?, pdam = ?, tipo = ?, sitmat = ?, sital = ? WHERE materia = ?''',
                           (reg[0], reg[1], reg[2], reg[3], reg[4], reg[5],
                            reg[6], reg[7], reg[8], reg[9], reg[10], reg[11],
                            reg[12], reg[13], reg[14]))
                data.commit()
            except sqlite3.Error as erro:
                print(erro)
            else:
                if reg[11] == 'F':
                    if ig[0] == 'diferente' and cond[0] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 01" alterada com sucesso para == {reg[0]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[0] == 'igual' and cond[0] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[1] == 'diferente' and cond[1] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 02" alterada com sucesso para == {reg[2]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[1] == 'igual' and cond[1] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[2] == 'diferente' and cond[2] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 03" alterada com sucesso para == {reg[4]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[2] == 'igual' and cond[2] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 03" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[2] == 'igual' and cond[2] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 03" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[2] == 'igual' and cond[2] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 03" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[2] == 'igual' and cond[2] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 03" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[3] == 'diferente' and cond[3] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 04" alterada com sucesso para == {reg[6]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[3] == 'igual' and cond[3] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 04" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[3] == 'igual' and cond[3] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 04" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[3] == 'igual' and cond[3] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 04" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[3] == 'igual' and cond[3] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 04" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[4] == 'diferente' and cond[4] == 'c':
                        Banco.linhas(f'Nota referente à "Simulado" alterada com sucesso para == {reg[8]}', cm,
                                     bx, 'ne')
                    else:
                        if ig[4] == 'igual' and cond[4] == 'v':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor vazio"', cm,
                                         bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'l':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor não numérico"', cm,
                                         bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'f':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'c':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'ne')
                else:
                    if ig[0] == 'diferente' and cond[0] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 01" alterada com sucesso para == {reg[0]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[0] == 'igual' and cond[0] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[0] == 'igual' and cond[0] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 01" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[1] == 'diferente' and cond[1] == 'c':
                        Banco.linhas(f'Nota referente à "Prova 02" alterada com sucesso para == {reg[2]}', cm,
                                     bx, 'mc')
                    else:
                        if ig[1] == 'igual' and cond[1] == 'v':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor vazio"', cm,
                                         bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'l':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor não numérico"', cm,
                                         bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'f':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'mc')
                        if ig[1] == 'igual' and cond[1] == 'c':
                            Banco.linhas(f'Nota referente à "Prova 02" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'mc')
                    if ig[4] == 'diferente' and cond[4] == 'c':
                        Banco.linhas(f'Nota referente à "Simulado" alterada com sucesso para == {reg[8]}', cm,
                                     bx, 'ne')
                    else:
                        if ig[4] == 'igual' and cond[4] == 'v':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor vazio"', cm,
                                         bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'l':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor não numérico"', cm,
                                         bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'f':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "valor fora do intervalo"',
                                         cm, bx, 'ne')
                        if ig[4] == 'igual' and cond[4] == 'c':
                            Banco.linhas(f'Nota referente à "Simulado" não alterada por ser "o mesmo valor"', cm,
                                         bx, 'ne')
            finally:
                c1.close()
                data.close()

    @staticmethod
    def alter(par1, par2, par3, par4, par5, sub1, sub2, sub3, sub4, sub5):
        ne = [sub1, sub2, sub3, sub4, sub5]
        tex = [par1, par2, par3, par4, par5]
        tex1 = list()
        notas = list()
        tipos = list()
        igua = list()
        final1 = list()
        if tex[0] != '':
            try:
                n1 = float(tex[0].strip())
                if 0 <= n1 <= 10:
                    av1 = n1
                else:
                    av1 = 13
            except(ValueError, TypeError):
                av2 = 13
                tex1.append(av2)
                tipos.append('l')
            else:
                if av1 == 13:
                    tex1.append(av1)
                    tipos.append('f')
                else:
                    tex1.append(av1)
                    tipos.append('c')
        else:
            av3 = -1.0
            tex1.append(av3)
            tipos.append('v')
        if tex[1] != '':
            try:
                n2 = float(tex[1].strip())
                if 0 <= n2 <= 10:
                    av4 = n2
                else:
                    av4 = 13
            except(ValueError, TypeError):
                av5 = 13
                tex1.append(av5)
                tipos.append('l')
            else:
                if av4 == 13:
                    tex1.append(av4)
                    tipos.append('f')
                else:
                    tex1.append(av4)
                    tipos.append('c')
        else:
            av6 = -1.0
            tex1.append(av6)
            tipos.append('v')
        if tex[2] != '':
            try:
                n3 = float(tex[2].strip())
                if 0 <= n3 <= 10:
                    av7 = n3
                else:
                    av7 = 13
            except(ValueError, TypeError):
                av8 = 13
                tex1.append(av8)
                tipos.append('l')
            else:
                if av7 == 13:
                    tex1.append(av7)
                    tipos.append('f')
                else:
                    tex1.append(av7)
                    tipos.append('c')
        else:
            av9 = -1.0
            tex1.append(av9)
            tipos.append('v')
        if tex[3] != '':
            try:
                n4 = float(tex[3].strip())
                if 0 <= n4 <= 10:
                    av10 = n4
                else:
                    av10 = 13
            except(ValueError, TypeError):
                av11 = 13
                tex1.append(av11)
                tipos.append('l')
            else:
                if av10 == 13:
                    tex1.append(av10)
                    tipos.append('f')
                else:
                    tex1.append(av10)
                    tipos.append('c')
        else:
            av12 = -1.0
            tex1.append(av12)
            tipos.append('v')
        if tex[4] != '':
            try:
                si = float(tex[4].strip())
                if 0 <= si <= 2:
                    av13 = si
                else:
                    av13 = 13
            except(ValueError, TypeError):
                av14 = 13
                tex1.append(av14)
                tipos.append('l')
            else:
                if av13 == 13:
                    tex1.append(av13)
                    tipos.append('f')
                else:
                    tex1.append(av13)
                    tipos.append('c')
        else:
            av15 = -1.0
            tex1.append(av15)
            tipos.append('v')
        dfg = tex1
        if dfg[0] != 13 and dfg[0] != -1.0:
            if dfg[0] != ne[0]:
                nr1 = dfg[0]
                notas.append(nr1)
                igua.append('diferente')
            else:
                nr1 = dfg[0]
                notas.append(nr1)
                igua.append('igual')
        else:
            if dfg[0] == -1.0:
                if dfg[0] != ne[0]:
                    nr1 = ne[0]
                    notas.append(nr1)
                    igua.append('igual')
                else:
                    nr1 = dfg[0]
                    notas.append(nr1)
                    igua.append('igual')
            else:
                nr1 = ne[0]
                notas.append(nr1)
                igua.append('igual')
        if dfg[1] != 13 and dfg[1] != -1.0:
            if dfg[1] != ne[1]:
                nr1 = dfg[1]
                notas.append(nr1)
                igua.append('diferente')
            else:
                nr1 = dfg[1]
                notas.append(nr1)
                igua.append('igual')
        else:
            if dfg[1] == -1.0:
                if dfg[1] != ne[1]:
                    nr1 = ne[1]
                    notas.append(nr1)
                    igua.append('igual')
                else:
                    nr1 = dfg[1]
                    notas.append(nr1)
                    igua.append('igual')
            else:
                nr1 = ne[1]
                notas.append(nr1)
                igua.append('igual')
        if dfg[2] != 13 and dfg[2] != -1.0:
            if dfg[2] != ne[2]:
                nr1 = dfg[2]
                notas.append(nr1)
                igua.append('diferente')
            else:
                nr1 = dfg[2]
                notas.append(nr1)
                igua.append('igual')
        else:
            if dfg[2] == -1.0:
                if dfg[2] != ne[2]:
                    nr1 = ne[2]
                    notas.append(nr1)
                    igua.append('igual')
                else:
                    nr1 = dfg[2]
                    notas.append(nr1)
                    igua.append('igual')
            else:
                nr1 = ne[2]
                notas.append(nr1)
                igua.append('igual')
        if dfg[3] != 13 and dfg[3] != -1.0:
            if dfg[3] != ne[3]:
                nr1 = dfg[3]
                notas.append(nr1)
                igua.append('diferente')
            else:
                nr1 = dfg[3]
                notas.append(nr1)
                igua.append('igual')
        else:
            if dfg[3] == -1.0:
                if dfg[3] != ne[3]:
                    nr1 = ne[3]
                    notas.append(nr1)
                    igua.append('igual')
                else:
                    nr1 = dfg[3]
                    notas.append(nr1)
                    igua.append('igual')
            else:
                nr1 = ne[3]
                notas.append(nr1)
                igua.append('igual')
        if dfg[4] != 13 and dfg[4] != -1.0:
            if dfg[4] != ne[4]:
                nr1 = dfg[4]
                notas.append(nr1)
                igua.append('diferente')
            else:
                nr1 = dfg[4]
                notas.append(nr1)
                igua.append('igual')
        else:
            if dfg[4] == -1.0:
                if dfg[4] != ne[4]:
                    nr1 = ne[4]
                    notas.append(nr1)
                    igua.append('igual')
                else:
                    nr1 = dfg[4]
                    notas.append(nr1)
                    igua.append('igual')
            else:
                nr1 = ne[4]
                notas.append(nr1)
                igua.append('igual')
        final0 = [notas, tipos, igua]
        for c in final0:
            for i in c:
                final1.append(i)
        return final1

    @staticmethod
    def mostrar():
        import sqlite3
        from time import sleep
        cm = 91
        mb = 91
        arg2 = None
        c = None
        data = None
        try:
            data = sqlite3.connect('data.db')
            c = data.cursor()
            c.execute('''SELECT * from data where mdf >= 0''')
        except sqlite3.Error as erro:
            print(erro)
        else:
            arg2 = c.fetchall()
        finally:
            c.close()
            data.close()
        if arg2 is not None:
            arg3 = []
            cont1 = 0
            for c in arg2:
                if cont1 == 0 or c[11] < arg3[-1][11]:
                    arg3.append(c)
                    cont1 += 1
                else:
                    pos = 0
                    while pos < len(arg3):
                        if c[11] >= arg3[pos][11]:
                            arg3.insert(pos, c)
                            break
                        pos += 1
            posi = 1
            temp = 0.001
            for v in arg3:
                if v != arg3[-1]:
                    if v == arg3[0]:
                        Banco.linhas(f'{posi}º LUGAR:', cm, 0, 'mc')
                        sleep(temp)
                        Banco.linhas(f'MATÉRIA: {v[0].upper()}', 0, 0, 'nm')
                        sleep(temp)
                        Banco.linhas(f'MÉDIA: {v[11]:.2f}', 0, mb, 'mb')
                        sleep(temp)
                        posi += 1
                    else:
                        if posi <= 9:
                            Banco.linhas(f'0{posi}º lugar:', cm, 0, 'mc')
                            sleep(temp)
                            Banco.linhas(f'Matéria: {v[0]}', 0, 0, 'nm')
                            sleep(temp)
                            Banco.linhas(f'Média: {v[11]:.2f}', 0, 0, 'nm')
                            sleep(temp)
                        else:
                            Banco.linhas(f'{posi}º lugar:', cm, 0, 'mc')
                            sleep(temp)
                            Banco.linhas(f'Matéria: {v[0]}', 0, 0, 'nm')
                            sleep(temp)
                            Banco.linhas(f'Média: {v[11]:.2f}', 0, 0, 'nm')
                            sleep(temp)
                        posi += 1
                else:
                    if posi <= 9:
                        Banco.linhas(f'0{posi}º lugar (Última colocação):', cm, 0, 'mc')
                        sleep(temp)
                        Banco.linhas(f'Matéria: {v[0]}', 0, 0, 'nm')
                        sleep(temp)
                        Banco.linhas(f'Média: {v[11]:.2f}', 0, mb, 'mb')
                        sleep(temp)
                    else:
                        Banco.linhas(f'{posi}º lugar (Última colocação):', cm, 0, 'mc')
                        sleep(temp)
                        Banco.linhas(f'Matéria: {v[0]}', 0, 0, 'nm')
                        sleep(temp)
                        Banco.linhas(f'Média: {v[11]:.2f}', 0, mb, 'mb')
                        sleep(temp)
                    posi += 1

    @staticmethod
    def carr_linha0(mat):
        import sqlite3
        data = sqlite3.connect('data.db')
        c1 = data.cursor()
        records = None
        try:
            c1.execute('''SELECT * from data where materia = ?''', (mat,))
        except sqlite3.Error as erro:
            print(erro)
        else:
            records = c1.fetchall()
        finally:
            c1.close()
            data.close()
        if records:
            valores = list()
            for t in records:
                for n in t:
                    valores.append(n)
            return valores
        else:
            return ['', '', '', '', '', '']

    @staticmethod
    def retiracasas(*listi):
        lista = listi
        lista1 = list()
        for i in range(0, len(lista), 1):
            if i == 0:
                lista1.append(str(lista[i]))
            if i == 1:
                lista1.append(int(lista[i]))
            if 2 <= i <= 11:
                lista1.append(_round(lista[i], 3))
            if i == 12:
                lista1.append(_round(lista[i], 2))
            if i == 13:
                lista1.append(str(lista[i]))
        return lista1

    @staticmethod
    def informations(n1, n2, n3, n4, sim, mat, ativar=False, pes=False):
        from random import randint
        from time import sleep
        calcular = ativar
        pesos = pes
        si = sim
        if si == -1.0:
            si = 0.0
        const7 = 7.0
        const6 = 6.51
        const10 = 10.0
        div = 1
        dvx = 1
        gh = 91
        cm = 91
        mb = 91
        lis0 = [n1, n2, n3, n4]
        lisnt1 = list()
        lisnt2 = list()
        lisnt3 = list()
        lisnt4 = list()
        lis1 = list()
        mat1 = mat
        start = False
        start1 = False
        if -1.0 in lis0:
            start = True
        if -2.0 in lis0:
            start1 = True
        cont = 0
        for nh in lis0:
            if nh == -1.0:
                lis0[cont] = 0.0
                cont += 1
                lis1.append('cn')
            else:
                cont += 1
                lis1.append('ncn')
        for c in range(0, 4):
            if c == 0:
                lisnt1.append(lis0[c])
            if c == 1:
                lisnt2.append(lis0[c])
            if c == 2:
                lisnt3.append(lis0[c])
            if c == 3:
                lisnt4.append(lis0[c])
        if start1 is True:
            if si == -1.0:
                med1 = lis0[0] * 7.0 / 10
                med2 = lis0[1] * 3.0 / 10
                med3 = lis0[2] * 4.00 / 10
                med4 = lis0[3] * 3.00 / 10
                medm = med1 + med2
            else:
                med1 = lis0[0] * 7.0 / 10
                med2 = lis0[1] * 3.0 / 10
                med3 = lis0[2] * 4.00 / 10
                med4 = lis0[3] * 3.00 / 10
                medm = med1 + med2 + si
        else:
            if si == -1.0:
                med1 = lis0[0] * 1.50 / 10
                med2 = lis0[1] * 1.50 / 10
                med3 = lis0[2] * 4.00 / 10
                med4 = lis0[3] * 3.00 / 10
                medm = med1 + med2 + med3 + med4
            else:
                med1 = lis0[0] * 1.50 / 10
                med2 = lis0[1] * 1.50 / 10
                med3 = lis0[2] * 4.00 / 10
                med4 = lis0[3] * 3.00 / 10
                medm = med1 + med2 + med3 + med4 + si
        if calcular is True:
            if start is True:
                if medm < const7:
                    if start1 is True:
                        falta7 = const7 - medm
                        falta6 = const6 - medm
                        descon7 = 0
                        descon6 = 0
                        ump7 = falta7 / 3000
                        ump6 = falta6 / 3000
                        m61 = m62 = 0
                        m71 = m72 = 0
                        while descon7 <= falta7:
                            if lis1[0] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 7.0 / 10
                                m71 += m7
                                descon7 += m7
                            if lis1[1] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 3.0 / 10
                                m72 += m7
                                descon7 += m7
                        mf17 = m71 * 10 / 7.0
                        mf27 = m72 * 10 / 3.0
                        lisnt1.append(mf17)
                        lisnt2.append(mf27)
                        while descon6 <= falta6:
                            if lis1[0] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 7.0 / 10
                                m61 += m6
                                descon6 += m6
                            if lis1[1] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 3.0 / 10
                                m62 += m6
                                descon6 += m6
                        mf16 = m61 * 10 / 7.0
                        mf26 = m62 * 10 / 3.0
                        lisnt1.append(mf16)
                        lisnt2.append(mf26)
                        y = (lisnt1, lisnt2)
                        print('=' * gh)
                        sleep(0.1)
                        if 'cn' not in lis1:
                            print(f'  Matéria : {mat1}             Média: {medm:.2f}             "Fechada"')
                            sleep(0.1)
                        else:
                            print(f'  Matéria : {mat1}             Média: {medm:.2f}             "Aberta"')
                            sleep(0.1)
                        Banco.linhas('Notas necessárias para atingir a média ( 7.0 ):', cm, 0, 'mc')
                        sleep(0.1)
                        if lis1[0] == 'cn':
                            if 0 < mf17 <= const10:
                                print(f'  Prova 01 == {y[0][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[1] == 'cn':
                            if 0 < mf27 <= const10:
                                print(f'  Prova 02 == {y[1][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        Banco.linhas('Notas necessárias para atingir a média para arredondamento ( 6.51 ):',
                                     cm, 0, 'mc')
                        sleep(0.1)
                        if lis1[0] == 'cn':
                            if 0 < mf16 <= const10:
                                print(f'  Prova 01 == {y[0][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[1] == 'cn':
                            if 0 < mf26 <= const10:
                                print(f'  Prova 02 == {y[1][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        print('=' * gh)
                    else:
                        falta7 = const7 - medm
                        falta6 = const6 - medm
                        descon7 = 0
                        descon6 = 0
                        ump7 = falta7 / 3000
                        ump6 = falta6 / 3000
                        m61 = m62 = m63 = m64 = 0
                        m71 = m72 = m73 = m74 = 0
                        cota = 0
                        while descon7 <= falta7:
                            if lis1[0] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 1.5 / 10
                                m71 += m7
                                descon7 += m7
                                cota += 1
                            if lis1[1] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 1.5 / 10
                                m72 += m7
                                descon7 += m7
                                cota += 1
                            if lis1[2] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 4.0 / 10
                                m73 += m7
                                descon7 += m7
                                cota += 1
                            if lis1[3] == 'cn':
                                ran = randint(dvx, div)
                                mult7 = ran * ump7
                                m7 = mult7 * 3.0 / 10
                                m74 += m7
                                descon7 += m7
                                cota += 1
                        mf17 = m71 * 10 / 1.5
                        mf27 = m72 * 10 / 1.5
                        mf37 = m73 * 10 / 4.0
                        mf47 = m74 * 10 / 3.0
                        lisnt1.append(mf17)
                        lisnt2.append(mf27)
                        lisnt3.append(mf37)
                        lisnt4.append(mf47)
                        while descon6 <= falta6:
                            if lis1[0] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 1.5 / 10
                                m61 += m6
                                descon6 += m6
                                cota += 1
                            if lis1[1] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 1.5 / 10
                                m62 += m6
                                descon6 += m6
                                cota += 1
                            if lis1[2] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 4.0 / 10
                                m63 += m6
                                descon6 += m6
                                cota += 1
                            if lis1[3] == 'cn':
                                ran = randint(dvx, div)
                                mult6 = ran * ump6
                                m6 = mult6 * 3.0 / 10
                                m64 += m6
                                descon6 += m6
                                cota += 1
                        mf16 = m61 * 10 / 1.5
                        mf26 = m62 * 10 / 1.5
                        mf36 = m63 * 10 / 4.0
                        mf46 = m64 * 10 / 3.0
                        lisnt1.append(mf16)
                        lisnt2.append(mf26)
                        lisnt3.append(mf36)
                        lisnt4.append(mf46)
                        y = (lisnt1, lisnt2, lisnt3, lisnt4)
                        print('=' * gh)
                        sleep(0.1)
                        if 'cn' not in lis1:
                            print(f'  Matéria : {mat1}             Média: {medm:.2f}             "Fechada"')
                            sleep(0.1)
                        else:
                            print(f'  Matéria : {mat1}             Média: {medm:.2f}             "Aberta"')
                            sleep(0.1)
                        Banco.linhas('Notas necessárias para atingir a média ( 7.0 ):', cm, 0, 'mc')
                        sleep(0.1)
                        if lis1[0] == 'cn':
                            if 0 < mf17 <= const10:
                                print(f'  Prova 01 == {y[0][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[1] == 'cn':
                            if 0 < mf27 <= const10:
                                print(f'  Prova 02 == {y[1][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[2] == 'cn':
                            if 0 < mf37 <= const10:
                                print(f'  Prova 03 == {y[2][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[3] == 'cn':
                            if 0 < mf47 <= const10:
                                print(f'  Prova 04 == {y[3][1]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        Banco.linhas('Notas necessárias para atingir a média para arredondamento ( 6.51 ):',
                                     cm, 0, 'mc')
                        sleep(0.1)
                        if lis1[0] == 'cn':
                            if 0 < mf16 <= const10:
                                print(f'  Prova 01 == {y[0][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[1] == 'cn':
                            if 0 < mf26 <= const10:
                                print(f'  Prova 02 == {y[1][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[2] == 'cn':
                            if 0 < mf36 <= const10:
                                print(f'  Prova 03 == {y[2][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        if lis1[3] == 'cn':
                            if 0 < mf46 <= const10:
                                print(f'  Prova 04 == {y[3][2]:.2f}')
                                sleep(0.1)
                            else:
                                print(f'  Fora do alcance')
                                sleep(0.1)
                        print('=' * gh)
                else:
                    Banco.linhas(f'Não há média faltante, sua média já é {medm:.2f}', cm, mb)
            else:
                Banco.linhas(f'Não há média pendente referente à matéria "{mat1}" para ser calculada!', cm, mb)
        if pesos is True:
            if start1 is True:
                if medm > 0:
                    pes1 = med1 * 100 / medm
                    pes2 = med2 * 100 / medm
                    pes3 = si * 100 / medm
                else:
                    pes1 = 0.0
                    pes2 = 0.0
                    pes3 = 0.0
                if 'cn' not in lis1:
                    Banco.linhas(f'Matéria : {mat1}             Média: {medm:.2f}             "Fechada"', cm, 0,
                                 'mc')
                    sleep(0.1)
                else:
                    Banco.linhas(f'Matéria : {mat1}             Média: {medm:.2f}             "Aberta"', cm, 0,
                                 'mc')
                    sleep(0.1)
                Banco.linhas(f'A prova  01  tem  em  pontos  percentuais  o  peso  de == {pes1:.1f} %', cm, 0, 'mc')
                sleep(0.1)
                Banco.linhas(f'A prova  02  tem  em  pontos  percentuais  o  peso  de == {pes2:.1f} %', 0, mb, 'mb')
                sleep(0.1)
                Banco.linhas(f'A prova (simulado) tem em pontos percentuais o peso de == {pes3:.1f} %', 0, mb, 'mb')
            else:
                if medm > 0:
                    pes1 = med1 * 100 / medm
                    pes2 = med2 * 100 / medm
                    pes3 = med3 * 100 / medm
                    pes4 = med4 * 100 / medm
                    pes5 = si * 100 / medm
                else:
                    pes1 = 0.0
                    pes2 = 0.0
                    pes3 = 0.0
                    pes4 = 0.0
                    pes5 = 0.0
                if 'cn' not in lis1:
                    Banco.linhas(f'Matéria : {mat1}             Média: {medm:.2f}             "Fechada"', cm, 0,
                                 'mc')
                    sleep(0.1)
                else:
                    Banco.linhas(f'Matéria : {mat1}             Média: {medm:.2f}             "Aberta"', cm, 0,
                                 'mc')
                    sleep(0.1)
                Banco.linhas(f'A prova  01  tem  em  pontos  percentuais  o  peso  de == {pes1:.1f} %', cm, 0, 'mc')
                sleep(0.1)
                Banco.linhas(f'A prova  02  tem  em  pontos  percentuais  o  peso  de == {pes2:.1f} %', 0, 0, 'nm')
                sleep(0.1)
                Banco.linhas(f'A prova  03  tem  em  pontos  percentuais  o  peso  de == {pes3:.1f} %', 0, 0, 'nm')
                sleep(0.1)
                Banco.linhas(f'A prova  04  tem  em  pontos  percentuais  o  peso  de == {pes4:.1f} %', 0, mb, 'mb')
                sleep(0.1)
                Banco.linhas(f'A prova (simulado) tem em pontos percentuais o peso de == {pes5:.1f} %', 0, mb, 'mb')
        return lisnt1, lisnt2, lisnt3, lisnt4

    @staticmethod
    def estat(*lista):
        from time import sleep
        cm = 91
        mb = 91
        temp = 0.0001
        mater = lista
        m = []
        p = []
        if '-1006' not in mater and '-1007' not in mater and '-1008' not in mater:
            cont = 0
            cont2 = 0
            mp = 0
            mm = 0
            for t in mater:
                for v in t:
                    Banco.linhas(f'Matéria: {v[0]}', cm, 0, 'mc')
                    sleep(temp)
                    Banco.linhas(f'Semestre: {v[1]}', 0, 0, 'nm')
                    sleep(temp)
                    if v[2] != -1.0:
                        Banco.linhas(f'Média final: {v[2]:.2f}', 0, 0, 'nm')
                        sleep(temp)
                    else:
                        Banco.linhas(f'Média final: "?"', 0, 0, 'nm')
                        sleep(temp)
                    if v[3] != -1.0:
                        Banco.linhas(f'Percentual de aproveitamento: {v[3]:.1f}%', 0, 0, 'nm')
                        sleep(temp)
                    else:
                        Banco.linhas(f'Percentual de aproveitamento: "?"', 0, 0, 'nm')
                        sleep(temp)
                    Banco.linhas(f'Situação da matéria: {v[4]}', 0, 0, 'nm')
                    sleep(temp)
                    Banco.linhas(f'Situação do aluno: {v[5]}', 0, 0, 'nm')
                    sleep(temp)
                    if cont == 0:
                        if v[4] == 'Concluída':
                            m = v
                            p = v
                            cont += 1
                            mp += v[3]
                            mm += v[2]
                    else:
                        if v[4] == 'Concluída':
                            if v[2] > m[2]:
                                m = v
                            if v[2] < p[2]:
                                p = v
                            cont += 1
                            mp += v[3]
                            mm += v[2]
                    cont2 += 1
            if len(m) > 0 and cont > 1:
                Banco.linhas(f'Sua menor média final: {p[2]:.2f}', cm, 0, 'mc')
                sleep(temp)
                Banco.linhas(f'Seu menor percentual de aproveitamento: {p[3]:.1f}%', 0, 0, 'nm')
                sleep(temp)
                Banco.linhas(f'Matéria: {p[0]}', 88, 88, 'nm')
                sleep(temp)
                Banco.linhas(f'Semestre: {p[1]}', 0, 0, 'nm')
                sleep(temp)
                Banco.linhas(f'Sua maior média final: {m[2]:.2f}', cm, 0, 'mc')
                sleep(temp)
                Banco.linhas(f'Seu maior percentual de aproveitamento: {m[3]:.1f}%', 0, 0, 'nm')
                sleep(temp)
                Banco.linhas(f'Matéria: {m[0]}', 88, 88, 'nm')
                sleep(temp)
                Banco.linhas(f'Semestre: {m[1]}', 0, mb, 'mb')
                sleep(temp)
            if cont > 0:
                Banco.linhas(f'Total de matérias listadas: {cont2}', cm, 0, 'mc')
                Banco.linhas(f'Total de mátérias concluídas (desta listagem): {cont}', 0, 0, 'nm')
                meperc = mp / cont
                memed = mm / cont
                Banco.linhas(f'Média geral entre todas as matérias concluídas(desta listagem): {memed:.2f}',
                             0, 0, 'nm')
                Banco.linhas(f'Média dos percentuais de aproveitamento entre todas as matéria concluídas'
                             f' (desta listagem): {meperc:.1f}%', 0, mb, 'mb')
            else:
                Banco.linhas(f'Total de mátérias listadas: {cont2}', cm, mb, 'ne')
        else:
            if '-1006' in mater:
                Banco.linhas(f'Não há dados com o semestre selecionado!', cm, mb, 'ne')
            if '-1007' in mater:
                Banco.linhas(f'Não há dados com a situação da matéria selecionada!', cm, mb, 'ne')
            if '-1008' in mater:
                Banco.linhas(f'Não há dados com a situação do aluno selecionada!', cm, mb, 'ne')

    @staticmethod
    def filtro(sm1=False, sm2=False, sm3=False, sm4=False, sm5=False, sm6=False,
               sitcon=False, sitem=False, sitacur=False,
               sitalap=False, sitalapar=False, sitalrep=False, sitalcurs=False, sitalind=False):
        import sqlite3
        cont = 1
        semes = sm1, sm2, sm3, sm4, sm5, sm6
        semes2 = []
        for i in semes:
            if i is True:
                semes2.append(cont)
                cont += 1
            else:
                cont += 1
        data = sqlite3.connect('data.db')
        c1 = data.cursor()
        records = []
        try:
            if len(semes2) == 0 or len(semes2) == 6:
                c1.execute('''SELECT materia, semestre, mdf, pdam, sitmat,
                              sital from data''')
                records1 = c1.fetchall()
                records += records1
            else:
                for v in semes2:
                    vl = v
                    c1.execute('''SELECT materia, semestre, mdf, pdam, sitmat,
                                      sital from data where semestre = ?''', (vl,))

                    records1 = c1.fetchall()
                    records += records1
        except sqlite3.Error as erro:
            print(erro)
        finally:
            c1.close()
            data.close()
        if len(records) > 0:
            sitmateria = sitcon, sitem, sitacur
            sitmateria2 = []
            for i, v in enumerate(sitmateria):
                if v is True:
                    if i == 0:
                        sitmateria2.append('Concluída')
                    if i == 1:
                        sitmateria2.append('Em curso')
                    if i == 2:
                        sitmateria2.append('À cursar')
            if len(sitmateria2) == 3 or len(sitmateria2) == 0:
                sitmateria2 = []
            records2 = []
            if len(sitmateria2) == 0:
                for v in records:
                    records2.append(v)
            else:
                for v in records:
                    if 'Concluída' in sitmateria2:
                        if v[4] == 'Concluída':
                            records2.append(v)
                    if 'Em curso' in sitmateria2:
                        if v[4] == 'Em curso':
                            records2.append(v)
                    if 'À cursar' in sitmateria2:
                        if v[4] == 'À cursar':
                            records2.append(v)
            if len(records2) > 0:
                sital = sitalap, sitalapar, sitalrep, sitalcurs, sitalind
                sital2 = []
                for i, v in enumerate(sital):
                    if v is True:
                        if i == 0:
                            sital2.append('Aprovado')
                        if i == 1:
                            sital2.append('Ap. arred.')
                        if i == 2:
                            sital2.append('Reprovado')
                        if i == 3:
                            sital2.append('Cursando')
                        if i == 4:
                            sital2.append('Indefinida')
                if len(sital2) == 5 or len(sital2) == 0:
                    sital2 = []
                records3 = []
                if len(sital2) == 0:
                    for v in records2:
                        records3.append(v)
                else:
                    for v in records2:
                        if 'Aprovado' in sital2:
                            if v[5] == 'Aprovado':
                                records3.append(v)
                        if 'Ap. arred.' in sital2:
                            if v[5] == 'Ap. arred.':
                                records3.append(v)
                        if 'Reprovado' in sital2:
                            if v[5] == 'Reprovado':
                                records3.append(v)
                        if 'Cursando' in sital2:
                            if v[5] == 'Cursando':
                                records3.append(v)
                        if 'Indefinida' in sital2:
                            if v[5] == 'Indefinida':
                                records3.append(v)
                if len(records3) > 0:
                    return records3
                else:
                    return '-1008'
            else:
                return '-1007'
        else:
            return '-1006'

    @staticmethod
    def delete(mat):
        import sqlite3
        try:
            data = sqlite3.connect('data.db')
            c = data.cursor()
            c.execute('''DELETE FROM data WHERE materia = ?''',
                      (mat,))
            data.commit()
        except sqlite3.Error as erro:
            print(erro)
        else:
            c.close()
            data.close()

    @staticmethod
    def x():
        import sqlite3
        c = None
        data = None
        medias = None
        try:
            data = sqlite3.connect('data.db')
            c = data.cursor()
            c.execute('''SELECT mdf from data where mdf >= 0''')
        except sqlite3.Error as erro:
            print(erro)
        else:
            medias = c.fetchall()
        finally:
            c.close()
            data.close()
        mdf = 0.0
        cont = 0
        for i in medias:
            for v in i:
                mdf += v
                cont += 1
        mdc = mdf / cont
        pdc = mdc * 100 / 10
        jll = [mdc, pdc]
        return jll

    @staticmethod
    def retiracasas1(*listi):
        lista = listi
        lista1 = list()
        for i in range(0, len(lista), 1):
            if i == 0:
                lista1.append(_round(lista[i], 3))
            if i == 1:
                lista1.append(_round(lista[i], 2))
        return lista1

    @staticmethod
    def medsem(s1, s2, s3, s4, s5, s6):
        import sqlite3
        from time import sleep
        todos = [s1, s2, s3, s4, s5, s6]
        todos1 = []
        ind = ind1 = ind2 = 0
        mater = mater1 = mater2 = 1
        cont = 1
        cm = 91
        mb = 91
        temp = 0.0001
        records = None
        data = None
        c = None
        for v in todos:
            if v is True:
                todos1.append(cont)
            cont += 1
        if len(todos1) == 1:
            try:
                data = sqlite3.connect('data.db')
                c = data.cursor()
                c.execute('''SELECT materia, mdf, pdam, sitmat from data where semestre = ?''', (todos1[0],))
            except sqlite3.Error as erro:
                print(erro)
            else:
                records = c.fetchall()
            finally:
                c.close()
                data.close()
            cont1 = 0
            cont2 = 0
            mdn = 0.0
            mda = 0.0
            lis1 = []
            lis2 = []
            lis3 = []
            Banco.linhas(f'Informações referente ao semestre 0{todos1[0]}:', cm, mb, 'ne')
            sleep(temp)
            for i, t in enumerate(records):
                if cont1 == 0:
                    Banco.linhas(f'Matérias que o compõem:', 0, 0, 'mb')
                    cont1 += 1
                    sleep(temp)
                Banco.linhas(f'{i + 1}ª - {t[0]}', 0, 0, 'nm')
                if t[3] == 'Concluída':
                    lis3.append(i + 1)
                    lis3.append(t[0])
                if t[3] == 'À cursar':
                    lis1.append(i + 1)
                    lis1.append(t[0])
                if t[3] == 'Em curso':
                    lis2.append(i + 1)
                    lis2.append(t[0])
                if t[1] >= 0:
                    mdn += t[1]
                    mda += t[2]
                    cont2 += 1
                sleep(temp)
            if mdn > 0 and mda > 0:
                mdn1 = mdn / cont2
                mda1 = mda / cont2
            else:
                mdn1 = 0.0
                mda1 = 0.0
            if len(lis1) == 0 and len(lis2) == 0:
                Banco.linhas(f'Das quais todas já foram concluídas.', cm, 0, 'mc')
                sleep(temp)
                Banco.linhas(f'Gerando uma média desse semestre de: {mdn1:.2f}', 0, 0, 'nm')
                sleep(temp)
                Banco.linhas(f'Com um percentual de aproveitamento de : {mda1:.1f}%', 0, mb, 'mb')
            else:
                if len(lis3) > 0:
                    fy = int(len(lis3) / 2)
                    Banco.linhas(f'MATÉRIAS JÁ CONCLUÍDAS:', cm, 0, 'mc')
                    sleep(temp)
                    for c in range(0, fy):
                        Banco.linhas(f'{lis3[ind2]}ª - {lis3[mater2]}', 0, 0, 'nm')
                        ind2 += 2
                        mater2 += 2
                        sleep(temp)
                if len(lis2) > 0:
                    fh = int(len(lis2) / 2)
                    Banco.linhas(f'SENDO QUE PERMANECE (EM CURSO):', cm, 0, 'mc')
                    sleep(temp)
                    for c in range(0, fh):
                        Banco.linhas(f'{lis2[ind]}ª - {lis2[mater]}', 0, 0, 'nm')
                        ind += 2
                        mater += 2
                        sleep(temp)
                if len(lis1) > 0:
                    fi = int(len(lis1) / 2)
                    Banco.linhas(f'SENDO QUE PERMANECE AINDA (À CURSAR):', cm, 0, 'mc')
                    sleep(temp)
                    for c in range(0, fi):
                        Banco.linhas(f'{lis1[ind1]}ª - {lis1[mater1]}', 0, 0, 'nm')
                        ind1 += 2
                        mater1 += 2
                        sleep(temp)
                Banco.linhas(f'Gerando uma média temporária de : {mdn1:.2f}', cm, 0, 'mc')
                sleep(temp)
                Banco.linhas(f'Com um percentual de aproveitamento temporário de : {mda1:.1f}%', 0, mb, 'mb')
        else:
            Banco.linhas(f'ERRO-Selecione apenas um "semestre" para ver o resultado !', cm, mb, 'ne')
