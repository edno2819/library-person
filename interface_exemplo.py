import PySimpleGUI as sg

sg.change_look_and_feel('DarkGrey2')

#--------------------------------------LOGIN--------------------------------------------------------------------------
login_layout=[
    [sg.Text('Bot StarS', size=(20, 1), justification='center', font=("Helvetica", 20), relief=sg.RELIEF_RIDGE)],
    [sg.Text('', size=(15, 1), font=("Helvetica", 15))],
    [sg.Text('Login',size=(7,0)),sg.Input(size=(30,0),key=("login"),do_not_clear=False)],
    [sg.Text('Senha',size=(7,0)),sg.Input(size=(30,0),key=("senha"),password_char='*',do_not_clear=False)],
    [sg.Text('      ',size=(7,0))],
    [sg.Text('      ',size=(14,0)),sg.Button('Confirmar',border_width=5,key=("bot_login"))]]
 
#-----------------------------------------CONFIGURAÇÕES------------------------------------------------------------------------------
def configuracoes():
    if login in contas_ativas:# or configs[0]=="1":
        conta1=[sg.Text("Conta:",size=(15, 1)),sg.Radio("Real","tipo_conta",key="real",size=(7, 1)),sg.Radio("Treino","tipo_conta",key="treino",size=(7, 1))]
    else:
        conta1=[sg.Text("Conta:",size=(15, 1)),sg.Radio("Treino","tipo_conta",key="treino",size=(7, 1))]
        tipo_conta="PRACTICE"

    configuracoes=[
        [sg.Text('Bot StarS', justification='right', size=(16, 1), font=("Helvetica", 25)),sg.Image('start_img1.png')],
        [sg.Text('_'  * 100, size=(70, 1))],      
        [sg.Text('Usuário:', font=("Helvetica", 13)),sg.Input(default_text=(perfil['first_name']),disabled=True,size=(7, 1),font=("Helvetica", 13)),
        sg.Text('Banca Real:', font=("Helvetica", 13)),sg.Input(default_text=(saldo_real),disabled=True,size=(9, 1),font=("Helvetica", 13)),
        sg.Text('Banca Treino:', font=("Helvetica", 13)),sg.Input(default_text=(saldo_treino),disabled=True,size=(9, 1),font=("Helvetica", 13))
        ],
        [sg.Text('_'  * 100, size=(70, 1))],      
        [sg.Text('Configurações:', size=(15, 1), font=("Helvetica", 15))],
        [sg.Text('', size=(15, 1))],
        conta1,
        [sg.Text('      ',size=(7,0))],
        [sg.Text("Fonte de Sinal:",size=(15, 1)), sg.InputCombo(('Nem um', 'Bandas de Bollinger', 'Estatégia ST/T5', 'Hype Moderado', 'Hype Agressivo'), size=(20, 1),default_value="Escolha")],
        [sg.Text("Filtro de Notícias:",size=(15, 1)),sg.Radio("Sim","filtro_news",key="filtro_news_s",size=(7, 1)),sg.Radio("Não","filtro_news",key="filtro_news_n",size=(7, 1))],
        [sg.Text("Lista de Sinais:",size=(15, 1)),sg.Radio("Sim","lista_sinais",key="lista_sinais_ativa",size=(7, 1)),sg.Radio("Não","lista_sinais",key="lista_sinais_desativa",size=(7, 1))],
        [sg.Text("Gerenciamento:",size=(15, 1)),sg.Radio("Mão Fixa","gerenciamento",key="mao_fixa",size=(7, 1)),sg.Radio("Soros","gerenciamento",key="soros",size=(7, 1)),sg.Radio("SorosGale","gerenciamento",key="sorosgale",size=(8, 1)),sg.Radio("Martingale","gerenciamento",key="martingale",size=(7, 1))],
        
        
        [sg.Text('PayOut Min:',size=(15,0)),sg.Input('0',size=(10,0),key=("payout_min"),justification='right', enable_events=True)],
        [sg.Text('Taxa de Acerto Min:',size=(15,0)),sg.Input('0',size=(10,0),key=("tx_acerto_min"),justification='right', enable_events=True)],
        [sg.Text('Valor da Entrada:',size=(15,0)),sg.Input('0',size=(10,0),key=("entrada_global"),justification='right', enable_events=True)],   
        [sg.Text('Stop Win:',size=(15,0)),sg.Input('0',size=(10,0),key=("stop_win"),justification='right', enable_events=True)],
        [sg.Text('Stop Loss:',size=(15,0)),sg.Input('0',size=(10,0),key=("stop_loss"),justification='right', enable_events=True)],
        [sg.Text('Stop Win Móvel:',size=(15,0)),sg.Input('0',size=(10,0),key=("stop_win_movel"),justification='right', enable_events=True)],#,default_value="Escolha")],
        [sg.Text('_'  * 100, size=(70, 1))],      
        [sg.Text('', size=(15, 1))],
        [sg.Text('',size=(28,1)),sg.Button('START',key="Iniciar",size=(10,1))],
        ] 


    inter = sg.Window('bot', configuracoes, icon="icon.ico")

    while True:
        event, values = inter.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        if event=="Iniciar":
            break

        # if last character in input element is invalid, remove it
        if event == "payout_min" and len(values["payout_min"])>0:
            if values["payout_min"][-1] not in ('0123456789.') or values["payout_min"][0] not in ('0123456789.'):
                inter["payout_min"].update(values["payout_min"][:-1])

        elif event == "tx_acerto_min" and len(values["tx_acerto_min"])>0:
            if values["tx_acerto_min"][-1] not in ('0123456789.') or values["tx_acerto_min"][0] not in ('0123456789.'):
                inter["tx_acerto_min"].update(values["tx_acerto_min"][:-1])

        elif event ==  "stop_win" and len(values[ "stop_win"])>0:
            if values["stop_win"][-1] not in ('0123456789.') or values[ "stop_win"][0] not in ('0123456789.'):
                inter["stop_win"].update(values["stop_win"][:-1])

        elif event ==  "stop_loss" and len(values["stop_loss"])>0:
            if values["stop_loss"][-1] not in ('0123456789.') or values["stop_loss"][0] not in ('0123456789.'):
                inter["stop_loss"].update(values["stop_loss"][:-1])

        elif event ==  "entrada_global" and len(values["entrada_global"])>0:
            if  values["entrada_global"][-1] not in ('0123456789.') or values["entrada_global"][0] not in ('0123456789.'):
                inter["entrada_global"].update(values["entrada_global"][:-1])

        elif event ==  "stop_win_movel" and len(values["stop_win_movel"])>0:
            if values["stop_win_movel"][-1] not in ('0123456789.') or values["stop_win_movel"][0] not in ('0123456789.'):
                inter["stop_win_movel"].update(values["stop_win_movel"][:-1])

    if mao_fixa:
        gerenciamento_tipo="Mão Fixa"

    elif soros:
        gere=[
        [sg.Text("Configurações do Gerenciamento:")],
        [sg.Text('Niveis de Soros:',size=(15,0)),sg.Input('1',size=(15,0),key=("nivel"), enable_events=True,justification="right")],
        [sg.Text('Fator de mutiplicação:',size=(15,0)),sg.Input('1.8',size=(15,0),key=("mutiplicacao"), enable_events=True,justification="right")],
        [sg.Button('Confirmar',border_width=5)]
        ]

        layout_gere = sg.Window('Gerenciamento config', gere)

        while True:
            event, values = layout_gere.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == "nivel" and len(values["nivel"])>0:
                if event == "nivel" and values["nivel"] and values["nivel"][-1] not in ('0123456789') or values["nivel"][0] not in ('0123456789'):
                    layout_gere["nivel"].update(values["nivel"][:-1])

            elif event == "mutiplicacao" and len(values["mutiplicacao"])>0:
                if event == "mutiplicacao" and values["mutiplicacao"] and values["mutiplicacao"][-1] not in ('0123456789.') or values["mutiplicacao"][0] not in ('0123456789.'):
                    layout_gere["mutiplicacao"].update(values["mutiplicacao"][:-1])


            if event=="Confirmar":
                nivel=int(values["nivel"])
                mutiplicacao=float(values["mutiplicacao"])
                gerenciamento_tipo="Soros"
                layout_gere.close() 

    elif sorosgale:
        gere=[
        [sg.Text("Configurações do Gerenciamento:")],
        [sg.Text('Niveis de SorosGale:',size=(15,0)),sg.Input("2",size=(15,0),key=("nivel"),justification="right", enable_events=True)],
        [sg.Button('Confirmar',border_width=5)]
        ]

        layout_gere = sg.Window('Gerenciamento config', gere)


        while True:
            event, values = layout_gere.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break        

            # if last character in input element is invalid, remove it
            if event == "nivel" and len(values["nivel"])>0:
                if event == "nivel" and values["nivel"] and values["nivel"][-1] not in ('0123456789') or values["nivel"][0] not in ('0123456789'):
                    layout_gere["nivel"].update(values["nivel"][:-1])

            if event=="Confirmar":
                nivel=int(values["nivel"])
                layout_gere.close()
                gerenciamento_tipo="SorosGale"  

    elif martingale:
        gere=[
        [sg.Text("Configurações do Gerenciamento:")],
        [sg.Text('Niveis de Soros:',size=(15,0)),sg.Input('1',size=(15,0),key=("nivel"), enable_events=True,justification="right")],
        [sg.Text('Fator de mutiplicação:',size=(15,0)),sg.Input('1.8',size=(15,0),key=("mutiplicacao"), enable_events=True,justification="right")],
        [sg.Button('Confirmar',border_width=5)]
        ]

        layout_gere = sg.Window('Gerenciamento config', gere)

        while True:
            event, values = layout_gere.read()

            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == "nivel" and len(values["nivel"])>0:
                if event == "nivel" and values["nivel"] and values["nivel"][-1] not in ('0123456789') or values["nivel"][0] not in ('0123456789'):
                    layout_gere["nivel"].update(values["nivel"][:-1])

            if event == "mutiplicacao" and len(values["mutiplicacao"])>0:
                if event == "mutiplicacao" and values["mutiplicacao"] and values["mutiplicacao"][-1] not in ('0123456789.') or values["mutiplicacao"][0] not in ('0123456789.'):
                    layout_gere["mutiplicacao"].update(values["mutiplicacao"][:-1])


            if event=="Confirmar":
                nivel=int(values["nivel"])
                mutiplicacao=float(values["mutiplicacao"])
                gerenciamento_tipo="SorosGale"
                layout_gere.close() 

    # if filtro_news:
    #     zonas_bloqueadas=scrap_news.get_zonas()
    # else:
    #     zonas_bloqueadas=[]

    inter.close()


def execucao():
    global layout3
    inter.close()
    layout_execut=[
    [sg.Text('Bot Eisen', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE),sg.Image('img_stars.png')],
    [sg.Text('_'  * 100, size=(70, 1))],
    [sg.Text('Conta:', font=("Helvetica", 13)),sg.Input(default_text=("Real" if tipo_conta=="REAL" else "Treino"),disabled=True,size=(7, 1),font=("Helvetica", 13)),
    sg.Text(f'Banca:',font=("Helvetica", 13)),sg.Input(default_text=API.get_balance(),key="banca",disabled=True,size=(10, 1),font=("Helvetica", 13)),
    sg.Text('Saldo Diário:',font=("Helvetica", 13)),sg.Input(default_text=saldo,key="saldo", disabled=True,size=(10, 1),font=("Helvetica", 13))],
    [sg.Text('',size=(25,1))],
    [sg.Text('',size=(27,1)),sg.Button('START',key="start",size=(10,1))],
    [sg.Text('_'  * 100, size=(70, 1))],
    [sg.Output(size=(80,20),background_color="Black",text_color="white",font=("Helvetica", 10))]
    ]
    layout3 = sg.Window('bot', layout_execut)
    # iniciando 
    threading.Thread(target=start).start()
    event, values = layout3.read()

#-------------------------------------------------------------------------------------------------------------------------------------------
def run():
    global API,login,senha,aviso,configs,contas_ativas
    logando = sg.Window('Login', login_layout, icon="icon.ico")
    aviso,configs,contas_ativas=clientes_ativos.iniciar_telegram_clientes()

    while True:
        event, values = logando.read()
        login="edno28@hotmail.com"#values["login"]
        senha="99730755ed"#values["senha"]
        API = IQ_Option(login,senha )
        API.connect()
        if API.check_connect() == False:
            sg.popup("Dados incorretos!")
            
        else:
            break

    logando.close()

    configuracoes() 

