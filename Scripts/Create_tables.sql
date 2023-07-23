create table if not exists profile(
	id serial primary key,
	vk_link varchar(500) not null,
	name varchar(255) not null,
	surname varchar(255),
	age integer,
	gender varchar(1) not null,
	city varchar(255),
	photo_1_link varchar(500) not null,
	photo_2_link varchar(500) not null,
	photo_3_link varchar(500) not null,
	constraint c_gender check (gender in ('М', 'Ж'))
);

create table if not exists cross_profiles (
	profile_id_1 integer not null references profile(id),
	profile_id_2 integer not null references profile(id),
	constraint profile_profile_pk primary key (profile_id_1, profile_id_2)
);
