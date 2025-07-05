INSERT INTO accounts (organization_id, account_number, name, creation_date, description)
VALUES %s
ON CONFLICT (account_number) DO NOTHING;