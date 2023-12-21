from odoo import http
from odoo.http import request, Response
import json


class Todos(http.Controller):
    @http.route('/todos', website=True, auth='public', methods=['GET'])
    def list(self, **kwargs):
        return request.render('todos.test_todo')


class Student(http.Controller):
    @http.route('/students', website=True, auth='public', methods=['GET'])
    def list(self, **kwargs):
        return request.render('todos.student_sec')

    @http.route('/students/add', website=True, auth='public', methods=['GET'])
    def add(self, **kwargs):
        return request.render('todos.add_student')

    @http.route('/students/update/<int:id>', website=True, auth='public', methods=['GET'])
    def update(self, id, **kwargs):
        return request.render('todos.update_student', {'id': id})


class TodosAPI(http.Controller):
    @http.route('/api/todos', auth='public', methods=['GET'])
    def list(self, **kwargs):
        records = request.env['todos.todo'].sudo().search_read([], ['id', 'name', 'is_completed'])
        data = json.dumps(records)
        return Response(data, content_type='application/json')

    @http.route('/api/todos/<int:id>', auth='public', methods=['GET'])
    def read(self, id, **kwargs):
        record = request.env['todos.todo'].sudo().browse(id)
        return Response(json.dumps(record.read(['name', 'is_completed'])), content_type='application/json')

    @http.route('/api/todos', auth='public', methods=['POST'], csrf=False)
    def create(self, **kwargs):
        json_bytes = request.httprequest.data
        json_string = json_bytes.decode('utf-8')
        data = json.loads(json_string)

        record = request.env['todos.todo'].sudo().create(data)
        return Response(json.dumps(record.read(['name', 'is_completed'])), content_type='application/json')

    @http.route('/api/todos/<int:id>', auth='public', methods=['PUT'], csrf=False, type='http')
    def update(self, id, **kwargs):
        json_bytes = request.httprequest.data
        json_string = json_bytes.decode('utf-8')
        data = json.loads(json_string)

        record = request.env['todos.todo'].sudo().browse(id)
        record.write(data)
        return Response(json.dumps(record.read(['name', 'is_completed'])), content_type='application/json')

    @http.route('/api/todos/<int:id>', auth='public', methods=['DELETE'], csrf=False)
    def delete(self, id, **kwargs):
        record = request.env['todos.todo'].sudo().browse(id)
        record.unlink()
        return "Record deleted successfully!"


class StudentAPI(http.Controller):
    @http.route('/api/student', auth='public', methods=['GET'])
    def list(self, **kwargs):
        records = request.env['todos.students'].sudo().search_read([], ['name', 'regi_no', 'mobile', 'department_id',
                                                                        'course_ids'])
        for record in records:
            course_ids = record.get('course_ids')
            if course_ids:
                courses_data = request.env['todos.course'].sudo().search_read([('id', 'in', course_ids)], ['name'])
                record['course_names'] = [{'id': course['id'], 'name': course['name']} for course in courses_data]

        data = json.dumps(records)

        return Response(data, content_type='application/json')

    @http.route('/api/student/<int:id>', auth='public', methods=['GET'])
    def read(self, id, **kwargs):
        record = request.env['todos.students'].sudo().browse(id)
        record_data = record.read(['name', 'regi_no', 'mobile', 'department_id', 'course_ids'])
        course_ids = record_data[0]['course_ids']
        if course_ids:
            courses_data = request.env['todos.course'].sudo().search_read([('id', 'in', course_ids)], ['name'])
            record_data[0]['course_names'] = [{'id': course['id'], 'name': course['name']} for course in courses_data]

        data = json.dumps(record_data[0])
        return Response(data, content_type='application/json')

    @http.route('/api/student', auth='public', methods=['POST'], csrf=False)
    def create(self, **kwargs):
        json_bytes = request.httprequest.data
        json_string = json_bytes.decode('utf-8')
        data = json.loads(json_string)

        record = request.env['todos.students'].sudo().create(data)
        return Response(json.dumps(record.read(['name', 'regi_no', 'mobile', 'department_id', 'course_ids'])),
                        content_type='application/json')

    @http.route('/api/student/<int:id>', auth='public', methods=['PUT'], csrf=False, type='http')
    def update(self, id, **kwargs):
        json_bytes = request.httprequest.data
        json_string = json_bytes.decode('utf-8')
        data = json.loads(json_string)

        record = request.env['todos.students'].sudo().browse(id)
        record.write(data)
        return Response(json.dumps(record.read(['name', 'regi_no', 'mobile', 'department_id', 'course_ids'])),
                        content_type='application/json')

    @http.route('/api/student/<int:id>', auth='public', methods=['DELETE'], csrf=False)
    def delete(self, id, **kwargs):
        record = request.env['todos.students'].sudo().browse(id)
        record.unlink()
        return "Record deleted successfully!"


class DepertmentAPI(http.Controller):
    @http.route('/api/department', auth='public', methods=['GET'])
    def list(self, **kwargs):
        records = request.env['todos.department'].sudo().search_read([], ['name'])
        data = json.dumps(records)
        return Response(data, content_type='application/json')


class CourseAPI(http.Controller):
    @http.route('/api/course', auth='public', methods=['GET'])
    def list(self, **kwargs):
        records = request.env['todos.course'].sudo().search_read([], ['name', 'department_id'])
        data = json.dumps(records)
        return Response(data, content_type='application/json')

    @http.route('/api/course/<int:id>', auth='public', methods=['GET'])
    def sorted(self, id, **kwargs):
        print(id)
        domain = [('department_id', '=', id)]
        records = request.env['todos.course'].sudo().search_read(domain, ['name', 'department_id'])
        data = json.dumps(records)
        return Response(data, content_type='application/json')
