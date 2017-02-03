-- This is a small fix on the default settings of the Italian language.
-- Unfortunately, this record doesn't have any external ID (because it's
-- created during the setup process), so it cannot be referenced through
-- a standard XML file.
UPDATE
    res_lang

SET
    date_format = '%d/%m/%Y',
    decimal_point = ',',
    grouping = '[3,0]',
    thousands_sep = '.'

WHERE
    code = 'it_IT'
