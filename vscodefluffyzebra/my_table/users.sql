create table users{
    user_id int primary key unique not null auto_increment,
    user_tag varchar(128)
    user_email varchar(128)
    user_password varchar(128)
}