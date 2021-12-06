from etherscan import Etherscan
eth = Etherscan("ZQX7BZJDX5TN1KFACWS3HRII29KB92267W") # key in quotation marks
key=input('Hello user \n This is ERC20 Helper 1.0 \n Input "help" for more information or detail,balanceOf,watch_tx,latest_tx,holders : ')
run="C"
while True:
    if key=='help':
        p="""Input "help"     --> for more information 
    ----- "Detail"    --> for show name, symbol and decimals of the target contract_address 
    ----- "balanceOf" --> for show the balanceOf target_address on the contract_address
    ----- "watch_tx"  --> for subscribe Tx from the contract_address in watching mode and constantly output the url link to etherscan.io
    ----- "latest_tx" --> for generate Latest N transaction (1 <= N <= 100) to a text file showing sender address, txHash, decoded call data
    ----- "holders"   --> for generate current top N holders (1 <= N <= 100) to a text file containing holder addresses and balances"""
        print(p)
        key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')
    elif key=='detail':
        contract_address =str(input('Input contract address : '))
        while True:
            if contract_address.count('') == 43: break
            else:
                contract_address =str(input('Please input correct contract address : '))
        token_detail=eth.get_erc20_token_transfer_events_by_address(contract_address,1,99999999,'asc')[0]
        name=token_detail['tokenName']
        symbol=token_detail['tokenSymbol']
        decimals=token_detail['tokenDecimal']
        print('Token name is '+name+', \nToken symbol is '+symbol+', \ndecimals is '+decimals)
        run=input('Continue(Any key) or Exit(E)')
        if not(run == 'Exit' or run=='E'):
            key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')   
    elif key=='balanceOf':
        contract_address =str(input('Input contract address : '))
        while True:
            if contract_address.count('') == 43: break
            else:
                contract_address =str(input('Please input correct contract address : '))
        target_address =str(input('Input target address : '))
        while True:
            if target_address.count('') == 43: break
            else:
                target_address =str(input('Please input correct target address : '))
        token_balance=eth.get_acc_balance_by_token_and_contract_address(contract_address,target_address)
        print('Balance0f of Account :',target_address,'=',float(token_balance)/1000000000000000000)
        run=input('Continue(Any key) or Exit(E)')
        if not(run == 'Exit' or run=='E'):
            key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')         
    elif key=='watch_tx':
        contract_address =str(input('Input contract address : '))
        while True:
            if contract_address.count('') == 43: break
            else:
                contract_address =str(input('Please input correct contract address : '))
        Subscribe = 'P'
        hash_start=eth.get_normal_txs_by_address(contract_address,13750000,99999999,'desc')[0]['hash']
        while True:
            hash_currect=eth.get_normal_txs_by_address(contract_address,13750000,99999999,'desc')[0]['hash']
            print('Wait for new Transaction')
            if hash_start != hash_currect:
                tx=hash_currect
                print('Url : https://etherscan.io/tx/'+tx)
                Subscribe=input('Continue(Any key), Exit(E)')
                hash_start=hash_currect
            if Subscribe == 'E' : break
        run=input('Continue(Any key) or Exit(E)')
        if not(run == 'Exit' or run=='E'):
            key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')        
    elif key=='latest_tx':
        contract_address =str(input('Input contract address : '))
        while True:
            if contract_address.count('') == 43: break
            else:
                contract_address =str(input('Please input correct contract address : '))
        N=int(input('N = '))
        f = open("latest_txfile.txt", "w")
        Storge=eth.get_normal_txs_by_address(contract_address,0,99999999,'desc')
        for n in range(N):
            txHash=Storge[n]['hash']
            sender=Storge[n]['from']
            f.write(str(n+1)+".Sender is "+sender+", txHash is "+txHash)
            f.write('\n')
        f.close()
        run=input('Continue(Any key) or Exit(E)')
        if not(run == 'Exit' or run=='E'):
            key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')        
    elif key=='holders':
        D=dict()
        s=set()
        list_balance=[]
        list_holder=[]
        dict_holder=dict()
        Holder=''
        contract_address =str(input('Input contract address : '))
        while True:
            if contract_address.count('') == 43: break
            else:
                contract_address =str(input('Please input correct contract address : '))
        N=int(input('N = '))
        f = open("Holderfile.txt", "w")
        Storge=eth.get_normal_txs_by_address(contract_address,0,99999999,'desc')
        for n in Storge:
            Holder=n['from']
            token_balance=int(eth.get_acc_balance_by_token_and_contract_address(contract_address,Holder))/1000000000000000000
            D[token_balance]=Holder
            s.add(token_balance)
        list_balance=sorted(s,reverse=True)
        for r in list_balance:
            list_holder.append(D[r])
        for i in range(N):
            print(i)
            dict_holder[list_holder[i]]=list_balance[i]
            print(dict_holder)
        n=0
        for k,v in dict_holder.items():
            f.write(str(n+1)+".Holder is "+str(k)+", Balance0f is "+str(v))
            f.write('\n')
            n=n+1
        f.close()
        run=input('Continue(Any key) or Exit(E)')
        if not(run == 'Exit' or run=='E'):
            key=input('help,detail,balanceOf,watch_tx,latest_tx,holders : ')
    else:
        key=input('Please input correct key (help,detail,balanceOf,watch_tx,latest_tx,holders) : ')
    if run in ('Exit', 'E'):
        break
    
