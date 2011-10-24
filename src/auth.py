


<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>src/auth.py at master from jwoschitz/python_basic_auth - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    
    

    <meta content="authenticity_token" name="csrf-param" />
<meta content="c5d6f4a8dc97a9027311e29ae2de85129bff825b" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/stylesheets/bundle_github.css?274c62b0fa5396961fbd444ea6b1ca3feb9e204f" media="screen" rel="stylesheet" type="text/css" />
    

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundle_jquery.js?feac705db7bad7450550f9b531ff2d76f0ce30c4" type="text/javascript"></script>

    <script src="https://a248.e.akamai.net/assets.github.com/javascripts/bundle_github.js?7267540807bb3adb6133264d22481c6bff644121" type="text/javascript"></script>

    

      <link rel='permalink' href='/jwoschitz/python_basic_auth/blob/ae21a5a18635a035e6225b3cb07c90c1872ab576/src/auth.py'>
    

    <meta name="description" content="python_basic_auth hosted on GitHub" />
  <link href="https://github.com/jwoschitz/python_basic_auth/commits/master.atom" rel="alternate" title="Recent Commits to python_basic_auth:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob windows env-production ">
    


    

    <div id="main">
      <div id="header" class="true">
          <a class="logo" href="https://github.com/">
            <img alt="github" class="default svg" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.svg" />
            <img alt="github" class="default png" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6.png" />
            <!--[if (gt IE 8)|!(IE)]><!-->
            <img alt="github" class="hover svg" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.svg" />
            <img alt="github" class="hover png" height="45" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov6-hover.png" />
            <!--<![endif]-->
          </a>

          


    <div class="userbox">
      <div class="avatarname">
        <a href="https://github.com/jwoschitz"><img src="https://secure.gravatar.com/avatar/a289e3e5a54426d3a172df981762f4ef?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20"  /></a>
        <a href="https://github.com/jwoschitz" class="name">jwoschitz</a>

      </div>
      <ul class="usernav">
        <li><a href="https://github.com/">Dashboard</a></li>
        <li>
          <a href="https://github.com/inbox">Inbox</a>
          <a href="https://github.com/inbox" class="unread_count ">0</a>
        </li>
        <li><a href="https://github.com/account">Account Settings</a></li>
        <li><a href="/logout">Log Out</a></li>
      </ul>
    </div><!-- /.userbox -->


        <div class="topsearch">
<form action="/search" id="top_search_form" method="get">      <a href="/search" class="advanced-search tooltipped downwards" title="Advanced Search">Advanced Search</a>
      <div class="search placeholder-field js-placeholder-field">
        <label class="placeholder" for="global-search-field">Search…</label>
        <input type="text" class="search my_repos_autocompleter" id="global-search-field" name="q" results="5" /> <input type="submit" value="Search" class="button" />
      </div>
      <input type="hidden" name="type" value="Everything" />
      <input type="hidden" name="repo" value="" />
      <input type="hidden" name="langOverride" value="" />
      <input type="hidden" name="start_value" value="1" />
</form>    <ul class="nav">
        <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
        <li><a href="https://gist.github.com">Gist</a></li>
        <li><a href="/blog">Blog</a></li>
      <li><a href="http://help.github.com">Help</a></li>
    </ul>
</div>

      </div>

      
            <div class="site">
      <div class="pagehead repohead vis-public   instapaper_ignore readability-menu">


      <div class="title-actions-bar">
        <h1>
          <a href="/jwoschitz">jwoschitz</a> /
          <strong><a href="/jwoschitz/python_basic_auth" class="js-current-repository">python_basic_auth</a></strong>
        </h1>
        



            <ul class="pagehead-actions">

          <li class="for-owner"><a href="/jwoschitz/python_basic_auth/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
            <a href="/jwoschitz/python_basic_auth/toggle_watch" class="minibutton btn-watch unwatch-button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'c5d6f4a8dc97a9027311e29ae2de85129bff825b'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Unwatch</span></a>
        </li>
            <li><a href="/jwoschitz/python_basic_auth/fork" class="minibutton btn-fork fork-button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'c5d6f4a8dc97a9027311e29ae2de85129bff825b'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>

            <li class="nspr">
              <a href="/jwoschitz/python_basic_auth/pull/new/master" class="minibutton btn-pull-request "><span><span class="icon"></span>Pull Request</span></a>
            </li>
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers watching">
            <a href="/jwoschitz/python_basic_auth/watchers" title="Watchers — You're Watching" class="tooltipped downwards">
              1
            </a>
          </li>
          <li class="forks">
            <a href="/jwoschitz/python_basic_auth/network" title="Forks - You have a fork" class="tooltipped downwards">
              1
            </a>
          </li>
        </ul>
      </li>
    </ul>

      </div>

        

  <ul class="tabs">
    <li><a href="/jwoschitz/python_basic_auth" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/jwoschitz/python_basic_auth/network" highlight="repo_networkrepo_fork_queue">Network</a>
    <li><a href="/jwoschitz/python_basic_auth/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/jwoschitz/python_basic_auth/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/jwoschitz/python_basic_auth/wiki" highlight="repo_wiki">Wiki <span class='counter'>0</span></a></li>

    <li><a href="/jwoschitz/python_basic_auth/graphs" highlight="repo_graphsrepo_contributors">Stats &amp; Graphs</a></li>

  </ul>

  
<div class="frame frame-center tree-finder" style="display:none"
      data-tree-list-url="/jwoschitz/python_basic_auth/tree-list/ae21a5a18635a035e6225b3cb07c90c1872ab576"
      data-blob-url-prefix="/jwoschitz/python_basic_auth/blob/ae21a5a18635a035e6225b3cb07c90c1872ab576"
    >

  <div class="breadcrumb">
    <b><a href="/jwoschitz/python_basic_auth">python_basic_auth</a></b> /
    <input class="tree-finder-input" type="text" name="query" autocomplete="off" spellcheck="false">
  </div>

    <div class="octotip">
      <p>
        <a href="/jwoschitz/python_basic_auth/dismiss-tree-finder-help" class="dismiss js-dismiss-tree-list-help" title="Hide this notice forever">Dismiss</a>
        <strong>Octotip:</strong> You've activated the <em>file finder</em>
        by pressing <span class="kbd">t</span> Start typing to filter the
        file list. Use <span class="kbd badmono">↑</span> and
        <span class="kbd badmono">↓</span> to navigate,
        <span class="kbd">enter</span> to view files.
      </p>
    </div>

  <table class="tree-browser" cellpadding="0" cellspacing="0">
    <tr class="js-header"><th>&nbsp;</th><th>name</th></tr>
    <tr class="js-no-results no-results" style="display: none">
      <th colspan="2">No matching files</th>
    </tr>
    <tbody class="js-results-list">
    </tbody>
  </table>
</div>

<div id="jump-to-line" style="display:none">
  <h2>Jump to Line</h2>
  <form>
    <input class="textfield" type="text">
    <div class="full-button">
      <button type="submit" class="classy">
        <span>Go</span>
      </button>
    </div>
  </form>
</div>


<div class="subnav-bar">

  <ul class="actions">
    
      <li class="switcher">

        <div class="context-menu-container js-menu-container">
          <span class="text">Current branch:</span>
          <a href="#"
             class="minibutton bigger switcher context-menu-button js-menu-target js-commitish-button btn-branch repo-tree"
             data-master-branch="master"
             data-ref="master">
            <span><span class="icon"></span>master</span>
          </a>

          <div class="context-pane commitish-context js-menu-content">
            <a href="javascript:;" class="close js-menu-close"></a>
            <div class="title">Switch Branches/Tags</div>
            <div class="body pane-selector commitish-selector js-filterable-commitishes">
              <div class="filterbar">
                <div class="placeholder-field js-placeholder-field">
                  <label class="placeholder" for="context-commitish-filter-field" data-placeholder-mode="sticky">Filter branches/tags</label>
                  <input type="text" id="context-commitish-filter-field" class="commitish-filter" />
                </div>

                <ul class="tabs">
                  <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                  <li><a href="#" data-filter="tags">Tags</a></li>
                </ul>
              </div>

                <div class="commitish-item branch-commitish selector-item">
                  <h4>
                      <a href="/jwoschitz/python_basic_auth/blob/master/src/auth.py" data-name="master">master</a>
                  </h4>
                </div>


              <div class="no-results" style="display:none">Nothing to show</div>
            </div>
          </div><!-- /.commitish-context-context -->
        </div>

      </li>
  </ul>

  <ul class="subnav">
    <li><a href="/jwoschitz/python_basic_auth" class="selected" highlight="repo_source">Files</a></li>
    <li><a href="/jwoschitz/python_basic_auth/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/jwoschitz/python_basic_auth/branches" class="" highlight="repo_branches">Branches <span class="counter">1</span></a></li>
    <li><a href="/jwoschitz/python_basic_auth/tags" class="blank" highlight="repo_tags">Tags <span class="counter">0</span></a></li>
    <li><a href="/jwoschitz/python_basic_auth/downloads" class="blank" highlight="repo_downloads">Downloads <span class="counter">0</span></a></li>
  </ul>

</div>

  
  
  


        

      </div><!-- /.pagehead -->

      




  
  <p class="last-commit">Latest commit to the <strong>master</strong> branch</p>

<div class="commit commit-tease js-details-container">
  <p class="commit-title ">
      <a href="/jwoschitz/python_basic_auth/tree/master/src"><a href="/jwoschitz/python_basic_auth/commit/ae21a5a18635a035e6225b3cb07c90c1872ab576" class="message">fixed unicode bug in MailDispatcher.send_mail and refactored some method...</a></a>
      <a href="javascript:;" class="minibutton expander-minibutton js-details-target"><span>…</span></a>
  </p>
    <div class="commit-desc"><pre>...s</pre></div>
  <div class="commit-meta">
    <a href="/jwoschitz/python_basic_auth/commit/ae21a5a18635a035e6225b3cb07c90c1872ab576" class="sha-block">commit <span class="sha">ae21a5a186</span></a>

    <div class="authorship">
      <img src="https://secure.gravatar.com/avatar/a289e3e5a54426d3a172df981762f4ef?s=140&d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="20" height="20" class="gravatar" />
      <span class="author-name"><a href="/jwoschitz">jwoschitz</a></span>
      authored <time class="js-relative-date" datetime="2011-10-24T01:23:47-07:00" title="2011-10-24 01:23:47">October 24, 2011</time>

    </div>
  </div>
</div>


  <div id="slider">

    <div class="breadcrumb" data-path="src/auth.py/">
      <b><a href="/jwoschitz/python_basic_auth/tree/ae21a5a18635a035e6225b3cb07c90c1872ab576" class="js-rewrite-sha">python_basic_auth</a></b> / <a href="/jwoschitz/python_basic_auth/tree/ae21a5a18635a035e6225b3cb07c90c1872ab576/src" class="js-rewrite-sha">src</a> / auth.py       <span style="display:none" id="clippy_21" class="clippy-text">src/auth.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_21&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://a248.e.akamai.net/assets.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_21&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div class="frames">
      <div class="frame frame-center" data-path="src/auth.py/" data-permalink-url="/jwoschitz/python_basic_auth/blob/ae21a5a18635a035e6225b3cb07c90c1872ab576/src/auth.py" data-title="src/auth.py at master from jwoschitz/python_basic_auth - GitHub" data-type="blob">
          <ul class="big-actions">
            <li><a class="file-edit-link minibutton js-rewrite-sha" href="/jwoschitz/python_basic_auth/edit/ae21a5a18635a035e6225b3cb07c90c1872ab576/src/auth.py" data-method="post"><span>Edit this file</span></a></li>
          </ul>

        <div id="files">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><img alt="Txt" height="16" src="https://a248.e.akamai.net/assets.github.com/images/icons/txt.png" width="16" /></span>
                <span class="mode" title="File Mode">100644</span>
                  <span>134 lines (110 sloc)</span>
                <span>5.427 kb</span>
              </div>
              <ul class="actions">
                <li><a href="/jwoschitz/python_basic_auth/raw/master/src/auth.py" id="raw-url">raw</a></li>
                  <li><a href="/jwoschitz/python_basic_auth/blame/master/src/auth.py">blame</a></li>
                <li><a href="/jwoschitz/python_basic_auth/commits/master/src/auth.py">history</a></li>
              </ul>
            </div>
              <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">from</span> <span class="nn">config</span> <span class="kn">import</span> <span class="n">Config</span></div><div class='line' id='LC2'><span class="kn">from</span> <span class="nn">database</span> <span class="kn">import</span> <span class="n">DbContext</span><span class="p">,</span> <span class="n">EmailAlreadyInUseError</span><span class="p">,</span> <span class="n">EmailTooLongError</span></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">exception</span> <span class="kn">import</span> <span class="n">Error</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">mail</span> <span class="kn">import</span> <span class="n">TemplateMailDispatcher</span><span class="p">,</span> <span class="n">MailDispatcher</span><span class="p">,</span> <span class="n">MailConfig</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">validator</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">crypto</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="k">class</span> <span class="nc">LoginResult</span><span class="p">:</span></div><div class='line' id='LC9'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">NONE</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">SUCCESS</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC11'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">USER_OR_PASSWORD_WRONG</span> <span class="o">=</span> <span class="mi">2</span></div><div class='line' id='LC12'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">USER_IS_NOT_ACTIVATED</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">USER_IS_LOCKED_OUT</span> <span class="o">=</span> <span class="mi">4</span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'><span class="k">class</span> <span class="nc">PasswordToShortError</span><span class="p">(</span><span class="n">Error</span><span class="p">):</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">min_chars</span><span class="p">):</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&quot;The password must be at least {0} characters long.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">min_chars</span><span class="p">))</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="k">class</span> <span class="nc">EmailIsInvalidError</span><span class="p">(</span><span class="n">Error</span><span class="p">):</span></div><div class='line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">):</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">super</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="s">&quot;The email address &#39;{0}&#39; contains invalid characters.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">email</span><span class="p">))</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC23'><span class="k">class</span> <span class="nc">Settings</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;password_min_length&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;login_attempt_expire&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;login_max_attempts&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;mail_activation_expire&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;mail_from&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;mail_subject&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;mail_body&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_set_attr_from_config</span><span class="p">(</span><span class="s">&quot;mail_body_html&quot;</span><span class="p">,</span> <span class="n">config</span><span class="p">)</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_set_attr_from_config</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">,</span> <span class="n">config</span><span class="p">):</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">value</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">config</span><span class="p">,</span><span class="n">attr_name</span><span class="p">)</span> <span class="k">if</span> <span class="n">config</span> <span class="k">else</span> <span class="bp">None</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">setattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">attr_name</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><span class="k">class</span> <span class="nc">AuthHandler</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>   </div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config_or_file_path</span><span class="p">):</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">config</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_config</span><span class="p">(</span><span class="n">config_or_file_path</span><span class="p">)</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_configure</span><span class="p">(</span><span class="n">config</span><span class="p">)</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_get_config</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config_or_file_path</span><span class="p">):</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">config_or_file_path</span><span class="p">,</span> <span class="n">Config</span><span class="p">):</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">config_or_file_path</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">Config</span><span class="p">(</span><span class="n">config_or_file_path</span><span class="p">)</span>                      </div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_configure</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">config</span><span class="p">):</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span> <span class="o">=</span> <span class="n">DbContext</span><span class="p">(</span><span class="n">config</span><span class="p">)</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">settings</span> <span class="o">=</span> <span class="n">Settings</span><span class="p">(</span><span class="n">config</span><span class="p">)</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mail_dispatcher</span> <span class="o">=</span> <span class="n">TemplateMailDispatcher</span><span class="p">(</span><span class="n">MailConfig</span><span class="p">(</span><span class="n">config</span><span class="p">),</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">mail_body</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">mail_body_html</span><span class="p">)</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">create_user</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="n">password</span><span class="p">)</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">activate_user</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">encoded_email</span><span class="p">,</span> <span class="n">activation_token</span><span class="p">):</span>        </div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">email</span> <span class="o">=</span> <span class="n">crypto</span><span class="o">.</span><span class="n">b64_decode</span><span class="p">(</span><span class="n">encoded_email</span><span class="p">)</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activated</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">activate</span><span class="p">(</span><span class="n">activation_token</span><span class="p">)</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">activated</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">resend_activation_email</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">):</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span><span class="o">.</span><span class="n">resend_activation_email</span><span class="p">()</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_user</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">):</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">User</span><span class="p">(</span><span class="n">email</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">mail_dispatcher</span><span class="p">)</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">login</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">user</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="n">password</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">user</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC78'><span class="k">class</span> <span class="nc">User</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>    </div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">email</span><span class="p">,</span> <span class="n">db_context</span><span class="p">,</span> <span class="n">settings</span><span class="p">,</span> <span class="n">mail_dispatcher</span><span class="p">):</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span> <span class="o">=</span> <span class="n">db_context</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">settings</span> <span class="o">=</span> <span class="n">settings</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mail_dispatcher</span> <span class="o">=</span> <span class="n">mail_dispatcher</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">email</span> <span class="o">=</span> <span class="n">email</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">is_logged_in</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">login_result</span> <span class="o">=</span> <span class="n">LoginResult</span><span class="o">.</span><span class="n">NONE</span></div><div class='line' id='LC86'><br/></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_is_activated</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">is_activated</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">is_activated</span> <span class="o">=</span> <span class="nb">property</span><span class="p">(</span><span class="n">get_is_activated</span><span class="p">)</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">create</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">validator</span><span class="o">.</span><span class="n">is_valid_email</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">):</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">EmailIsInvalidError</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span>   </div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">password</span><span class="p">)</span> <span class="o">&lt;</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">password_min_length</span><span class="p">):</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="n">PasswordToShortError</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">password_min_length</span><span class="p">)</span>     </div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activation_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">create</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> <span class="n">password</span><span class="p">)</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_send_activation_token</span><span class="p">(</span><span class="n">activation_token</span><span class="p">)</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">resend_activation_email</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activation_token</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">renew_activation_token</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_send_activation_token</span><span class="p">(</span><span class="n">activation_token</span><span class="p">)</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_send_activation_token</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">activation_token</span><span class="p">):</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">activation_token</span><span class="p">:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">encoded_email</span> <span class="o">=</span> <span class="n">crypto</span><span class="o">.</span><span class="n">b64_encode</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">mail_dispatcher</span><span class="o">.</span><span class="n">send_mail</span><span class="p">(</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">mail_from</span><span class="p">,</span> </div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> </div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">mail_subject</span><span class="p">,</span> </div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">{</span><span class="s">&quot;{ACTIVATION_TOKEN}&quot;</span><span class="p">:</span> <span class="n">activation_token</span><span class="p">,</span> <span class="s">&quot;{EMAIL_IDENTIFIER}&quot;</span><span class="p">:</span> <span class="n">encoded_email</span><span class="p">})</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">activate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">activation_token</span><span class="p">):</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">activated</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">activate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> <span class="n">activation_token</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">mail_activation_expire</span><span class="p">)</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">activated</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">login</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">password</span><span class="p">):</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">login_attempt</span><span class="o">.</span><span class="n">is_locked_out</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">login_attempt_expire</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">login_max_attempts</span><span class="p">):</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">login_result</span> <span class="o">=</span> <span class="n">LoginResult</span><span class="o">.</span><span class="n">USER_IS_LOCKED_OUT</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">login_attempt</span><span class="o">.</span><span class="n">log_failed_attempt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_activated</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">login_result</span> <span class="o">=</span> <span class="n">LoginResult</span><span class="o">.</span><span class="n">USER_IS_NOT_ACTIVATED</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">is_logged_in</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">user</span><span class="o">.</span><span class="n">login</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">,</span> <span class="n">password</span><span class="p">)</span>            </div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">is_logged_in</span><span class="p">:</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">login_result</span> <span class="o">=</span> <span class="n">LoginResult</span><span class="o">.</span><span class="n">SUCCESS</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">login_result</span> <span class="o">=</span> <span class="n">LoginResult</span><span class="o">.</span><span class="n">USER_OR_PASSWORD_WRONG</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_db_context</span><span class="o">.</span><span class="n">login_attempt</span><span class="o">.</span><span class="n">log_failed_attempt</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">email</span><span class="p">)</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span>            </div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>
    </div>

  </div>

<div class="frame frame-loading" style="display:none;" data-tree-list-url="/jwoschitz/python_basic_auth/tree-list/ae21a5a18635a035e6225b3cb07c90c1872ab576" data-blob-url-prefix="/jwoschitz/python_basic_auth/blob/ae21a5a18635a035e6225b3cb07c90c1872ab576">
  <img src="https://a248.e.akamai.net/assets.github.com/images/modules/ajax/big_spinner_336699.gif" height="32" width="32">
</div>

    </div>

    </div>

    <!-- footer -->
    <div id="footer" >
      
  <div class="upper_footer">
     <div class="site" class="clearfix">

       <!--[if IE]><h4 id="blacktocat_ie">GitHub Links</h4><![endif]-->
       <![if !IE]><h4 id="blacktocat">GitHub Links</h4><![endif]>

       <ul class="footer_nav">
         <h4>GitHub</h4>
         <li><a href="https://github.com/about">About</a></li>
         <li><a href="https://github.com/blog">Blog</a></li>
         <li><a href="https://github.com/features">Features</a></li>
         <li><a href="https://github.com/contact">Contact &amp; Support</a></li>
         <li><a href="https://github.com/training">Training</a></li>
         <li><a href="http://status.github.com/">Site Status</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Tools</h4>
         <li><a href="http://mac.github.com/">GitHub for Mac</a></li>
         <li><a href="http://mobile.github.com/">Issues for iPhone</a></li>
         <li><a href="https://gist.github.com">Gist: Code Snippets</a></li>
         <li><a href="http://fi.github.com/">Enterprise Install</a></li>
         <li><a href="http://jobs.github.com/">Job Board</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Extras</h4>
         <li><a href="http://shop.github.com/">GitHub Shop</a></li>
         <li><a href="http://octodex.github.com/">The Octodex</a></li>
       </ul>

       <ul class="footer_nav">
         <h4>Documentation</h4>
         <li><a href="http://help.github.com/">GitHub Help</a></li>
         <li><a href="http://developer.github.com/">Developer API</a></li>
         <li><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></li>
         <li><a href="http://pages.github.com/">GitHub Pages</a></li>
       </ul>

     </div><!-- /.site -->
  </div><!-- /.upper_footer -->

<div class="lower_footer">
  <div class="site" class="clearfix">
    <!--[if IE]><div id="legal_ie"><![endif]-->
    <![if !IE]><div id="legal"><![endif]>
      <ul>
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
      </ul>

      <p>&copy; 2011 <span id="_rrt" title="0.07986s from fe4.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    </div><!-- /#legal or /#legal_ie-->

      <div class="sponsor">
        <a href="http://www.rackspace.com" class="logo">
          <img alt="Dedicated Server" height="36" src="https://a248.e.akamai.net/assets.github.com/images/modules/footer/rackspace_logo.png?v2" width="38" />
        </a>
        Powered by the <a href="http://www.rackspace.com ">Dedicated
        Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
        Computing</a> of Rackspace Hosting<span>&reg;</span>
      </div>
  </div><!-- /.site -->
</div><!-- /.lower_footer -->

    </div><!-- /#footer -->

    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle select target</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column middle">
        <dl class="keyboard-mappings">
          <dt>I</dt>
          <dd>Mark selected as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>U</dt>
          <dd>Mark selected as unread</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>e</dt>
          <dd>Close selected</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Remove selected from view</dd>
        </dl>
      </div><!-- /.column.middle -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selected down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selected up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>
</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:
> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>

    <div class="context-overlay"></div>

    
    
    
  </body>
</html>

