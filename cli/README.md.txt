*****Installation*****
First, please install "pip install Etherscan" in cmd will use "py -m pip install Etherscan".
And then,create API acconut in Etherscan on this url "https://etherscan.io/apis"(API in this coding is my API)

--------------------------------------------------------------------------------------------

*****Start!!*****
Input keywords (help,detail,balanceOf,watch_tx,latest_tx,holders) that user want.

information
1."help" : show more information of each keywords
---input keywords again

2."Detail" : show name, symbol and decimals of the target contract_address 
---input contract_address.
---output token_name, symbol and decimal.
---input Continue(Any key) or Exit(E) for use this program again or exit.

3."balanceOf" : show the balanceOf target_address on the contract_address
---input contract_address and target_address.
---output token_balance.
---input Continue(Any key) or Exit(E) for use this program again or exit.

4."watch_tx" : subscribe Tx from the contract_address in watching mode and constantly output the url link to etherscan.io
---input contract_address.
---output url of that transaction.
---input Continue(Any key) or Exit(E) for continue watch_tx or exit.
---input Continue(Any key) or Exit(E) for use this program again or exit.

5."latest_tx" : generate Latest N transaction (1 <= N <= 100) to a text file showing sender address, txHash, decoded call data
---input contract_address and number of transactions.
---output text file including account of sender and transaction hash.
---input Continue(Any key) or Exit(E) for use this program again or exit.

6."holders" : generate current top N holders (1 <= N <= 100) to a text file containing holder addresses and balances
---input contract_address and number of transactions.
---output text file including account of holder and token balance.
---input Continue(Any key) or Exit(E) for use this program again or exit.
**** holders spend too much time to generate text file because I try to coding ****
