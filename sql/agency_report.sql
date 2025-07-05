INSERT INTO agency_reports (file_name, date, uploaded_at)
VALUES (%(file_name)s, %(date)s, %(uploaded_at)s)
ON CONFLICT (file_name) DO NOTHING;
-- RETURNING id;

SELECT id 
FROM agency_reports a
WHERE %(file_name)s = a.file_name;

