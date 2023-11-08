CREATE TABLE user_dependents
(
    id bigint,
    name character varying(200),
    relationship character varying(50),
    birth date,
    created_at timestamp,
    status "char",
    updated_at timestamp,
    deleted_at timestamp
)