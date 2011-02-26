<h1 style="text-align: center">Tags</h1>

  %if error:
    <p class="error">
    {{error}}
    </div>
  %end

<ul>
  %for tag in tags:
  %if not tag.startswith('.'):
  <li><a href="/tags?tags={{tag}}">{{tag}}</a></li>
  %end
  %end
</ul>
%rebase layout
