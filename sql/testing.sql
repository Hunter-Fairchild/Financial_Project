INSERT INTO accounts (account_number, account_name, creation_date, description)
SELECT v.account_number, v.account_name, v.creation_date::date, v.description
FROM (
    VALUES 
        ('70-00-0819', 'Hunter Account',       NULL, 'Testing Account'),
        ('10-00-9779', 'Anime Account',        NULL, 'Testing Anime Account for this testing db.'),
        ('10-00-9786', 'Paranormal Account',   NULL, 'Testing Paranormal Account for this testing db.')
) AS v(account_number, account_name, creation_date, description)
WHERE NOT EXISTS (
    SELECT 1 
    FROM accounts a 
    WHERE a.account_number = v.account_number
);

-- ON CONFLICT (account_number) DO NOTHING;


-- INSERT INTO organizations (organization_name, funding_category, creation_date, advisor, member_count, description)
-- VALUES ('Hunter''s Para', NULL, NULL, 'Cindy', 30, 'test');

UPDATE accounts
SET organization_id = 3
WHERE account_id = 7;

SELECT 
	a.account_number, 
	a.account_id,
	a.account_name,
	CASE
		WHEN o.organization_name IS NULL THEN 'None'
		ELSE o.organization_name
	END
FROM accounts a 
LEFT JOIN organizations o
	ON a.organization_id=o.organization_id;
-- SELECT * FROM organizations;

