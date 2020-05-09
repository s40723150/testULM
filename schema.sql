drop table if exists grouping;
create table grouping(
	id integer primary key autoincrement,
	user text not null,
        date text not null,
        result text not null,
	memo text
);