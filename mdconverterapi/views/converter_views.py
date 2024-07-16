from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from markdownify import markdownify as md
import markdown


@api_view(["POST"])
@permission_classes([AllowAny])
def markdown_to_html(request):
    """Converts markdown to HTML

    Method arguments:
      request -- The full HTTP request object
    """
    try:
        md_string = request.data["markdown"]
        html = markdown.markdown(md_string)
        return Response({"html": html}, status=status.HTTP_200_OK)
    except KeyError as ex:
        return Response(
            {"message": f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def html_to_markdown(request):
    """Converts HTML to Markdown

    Method arguments:
      request -- The full HTTP request object
    """
    try:
        html_string = request.data["html"]
        md_string = md(html_string, heading_style="ATX")
        return Response({"markdown": md_string}, status=status.HTTP_200_OK)
    except KeyError as ex:
        return Response(
            {"message": f"{ex.args[0]} is required"}, status=status.HTTP_400_BAD_REQUEST
        )
