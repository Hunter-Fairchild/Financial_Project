INSERT INTO balance_updates AS b (
    account_id, 
    report_id, 
    date, 
    opening_balance, 
    cactivity, 
    ending_balance
)
SELECT a.id, %(report_id)s, %(date)s, %(opening_balance)s, %(cactivity)s, %(ending_balance)s
FROM accounts a
WHERE a.account_number = %(account_number)s
ON CONFLICT (account_id, report_id) DO update
SET 
    date = %(date)s, 
    opening_balance = %(opening_balance)s, 
    cactivity = %(cactivity)s,
    ending_balance = %(ending_balance)s;