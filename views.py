from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

# 🚀 1. Create a Task
class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# 🚀 2. Assign a Task to Users
class AssignTaskView(APIView):
    def post(self, request):
        task_id = request.data.get("task_id")
        user_ids = request.data.get("user_ids", [])

        # Validate task existence
        task = get_object_or_404(Task, id=task_id)

        # Validate users existence
        users = User.objects.filter(id__in=user_ids)
        if not users.exists():
            return Response({"error": "One or more users not found"}, status=status.HTTP_404_NOT_FOUND)

        task.users.set(users)  # Assign users to the task
        task.save()
        return Response({"message": "Task assigned successfully!", "task": TaskSerializer(task).data}, status=status.HTTP_200_OK)

# 🚀 3. Get Tasks Assigned to a Specific User
class UserTasksView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 🚀 4. Get All Tasks (Optional)
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# 🚀 5. Get Task Details (Optional)
class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# 🚀 6. Update a Task
class TaskUpdateView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# 🚀 7. Delete a Task
class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
