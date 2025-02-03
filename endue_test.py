s = input().strip()

transactions = []
i = 0
while i < len(s):
    # Parse note (letters)
    note_start = i
    while i < len(s) and s[i].isalpha():
        i += 1
    note = s[note_start:i]
    
    # Parse amount (digits, commas, periods)
    amount_start = i
    while i < len(s) and (s[i].isdigit() or s[i] in ',.'):
        i += 1
    amount_str = s[amount_start:i]
    
    transactions.append((note, amount_str))

def parse_amount(amount_str):
    if '.' in amount_str:
        dollar_part, cent_part = amount_str.split('.', 1)
        cent = int(cent_part)
    else:
        dollar_part = amount_str
        cent = 0
    dollar = int(dollar_part.replace(',', ''))
    return dollar * 100 + cent

total_cents = 0
for _, amount_str in transactions:
    total_cents += parse_amount(amount_str)

def format_dollar_part(dollar):
    s = str(dollar)
    reversed_s = s[::-1]
    chunks = []
    for i in range(0, len(reversed_s), 3):
        chunk = reversed_s[i:i+3][::-1]
        chunks.append(chunk)
    chunks = chunks[::-1]
    return ','.join(chunks)

dollars = total_cents // 100
cents = total_cents % 100

if cents == 0:
    formatted = format_dollar_part(dollars)
else:
    formatted = f"{format_dollar_part(dollars)}.{cents:02d}"

print(formatted)