"""
Code generated by a tool. DO NOT EDIT.
https://sqldalmaker.sourceforge.net/
"""

from dbal.project import Project
from dbal.project_li import ProjectLi


class ProjectsDao:

    def __init__(self, ds):
        self.ds = ds

    def create_project(self, p):
        """
        (C)RUD: projects
        Generated values are passed to DTO.
        :param p: Project
        :return: None
        :raises Exception: if no rows inserted.
        """
        sql = """insert into projects (p_name) values (?)"""
        _ai_values = [["p_id", None]]
        self.ds.insert_row(sql, [p.p_name], _ai_values)
        p.p_id = _ai_values[0][1]

    def read_project_list(self):
        """
        C(R)UD: projects
        :return: list[Project]
        """
        sql = """select * from projects"""

        _res = []

        def _map_cb(row):
            _obj = Project()
            _obj.p_id = row["p_id"]  # t <- t
            _obj.p_name = row["p_name"]  # t <- t
            _res.append(_obj)

        self.ds.query_all_rows(sql, [], _map_cb)

        return _res

    def read_project(self, p_id, obj):
        """
        C(R)UD: projects
        :param p_id: int
        :param obj: Project
        :return: None on success or error string
        """
        sql = """select * from projects where p_id=?"""

        row = self.ds.query_row(sql, [p_id])
        if isinstance(row, str):
            return row
        obj.p_id = row["p_id"]  # t <- t
        obj.p_name = row["p_name"]  # t <- t

    def update_project(self, p):
        """
        CR(U)D: projects
        :param p: Project
        :return: int (the number of affected rows)
        """
        sql = """update projects set p_name=? where p_id=?"""

        return self.ds.exec_dml(sql, [p.p_name, p.p_id])

    def delete_project(self, p_id):
        """
        CRU(D): projects
        :param p_id: int
        :return: int (the number of affected rows)
        """
        sql = """delete from projects where p_id=?"""

        return self.ds.exec_dml(sql, [p_id])

    def get_projects(self):
        """
        :return: list[ProjectLi]
        """
        sql = """select p.*, 
                (select count(*) from tasks where p_id=p.p_id) as p_tasks_count 
                from projects p 
                order by p.p_id"""

        _res = []

        def _map_cb(row):
            _obj = ProjectLi()
            _obj.p_id = row["p_id"]  # q <- q
            _obj.p_name = row["p_name"]  # q <- q
            _obj.p_tasks_count = row["p_tasks_count"]  # q <- q
            _res.append(_obj)

        self.ds.query_all_rows(sql, [], _map_cb)

        return _res
