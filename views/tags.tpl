<h1 style="text-align: center">bookmarked under {{' and '.join(tag)}}</h1>

  %if error:
    <p class="error">
    {{error}}
    </div>
  %end

<dl>
  %for entry in bookmarks:
  <dt>{{entry[1]}}</dt>
  <dd><a href="{{entry[0]}}">{{entry[0]}}</a> <a href="/content/{{entry[2]}}">(Cache)</a></dd>
  %end
</dl>
%rebase layout
