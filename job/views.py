import os

from django.views import View
from django.conf import settings

from core.utils import GenId
from core.utils import Validator
from core.utils import ResponseMixin
from core.tasks import Dispatcher

from .models import JobInfo


Dispatcher().pop()


class UploadJob(ResponseMixin, View):
    """上传任务
    """

    def post(self, request):
        job_id = GenId.gen()
        name = request.POST.get("name")
        job = request.FILES.get('job')
        file_name = job.name

        file_path = os.path.join(settings.MEDIA_ROOT,
                                 'upload',
                                 file_name)

        with open(file_path, "wb") as file:
            for chunk in job.chunks():
                file.write(chunk)

        if not name:
            name = file_name

        job_info = {
            "job_id": job_id,
            "name": name,
        }
        JobInfo.objects.create(**job_info)

        Dispatcher(job_id, file_path).push()

        data = {
            "job_id": job_id
        }

        return self.get_json_response(data)


class JobList(ResponseMixin, View):
    """任务列表
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        user_id = validator.arg_check(
            arg_key="userId",
            arg_type=int)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            job_infos = JobInfo.objects.filter(is_deleted=False, user_id=user_id)

            data = list()
            for info in job_infos:
                data_tmp = dict()
                data_tmp["job_id"] = info.job_id
                data_tmp["name"] = info.name
                data_tmp["status"] = info.get_status_display()
                data_tmp["modified"] = info.modified

                data.append(data_tmp)

            return self.get_json_response(data)
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()
