function compress(str) {
  
if (!str) {throw new Error('empty/null string not allowed'); }

var lowerCases = /^[a-z]+$/;
var currentChar = str[0];
var currentCharCount = 0 ;
var result = [];

if(str.match(lowerCases)) {
	
   for (var i = 0, len = str.length; i < len; i++) {
	   
	   if( len-i == 1) {
		   currentCharCount++;
		   result.push(currentChar+currentCharCount);
		   return result.join('');
	   }
	   
		if(currentChar == str[i]) {
			currentCharCount++;
		} else {
			result.push(currentChar+currentCharCount);
			currentCharCount = 1;
			currentChar = str[i];
		}
		
	}
	
 }
else
  { 
   throw new Error('string with only lower case letters allowed'); 
  }
  
}
 
 compress('aaaabbaaaababbbcccccccccccc');
 
 
    function parseURL(url) {
        var parser = document.createElement('a'),
            searchObject = {},
            queries, split, i, queryString, equivalentQueries = false, repeatedQueriesKeys = false;
			
        // Let the browser do the work
        parser.href = decodeURI(url);
		
        // Convert query string to object
        queries = parser.search.replace(/^\?/, '').split('&');
		
        for( i = 0; i < queries.length; i++ ) {
            split = queries[i].split('=');
			if( Object.keys(searchObject).indexOf(split[0]) != -1 ) {
				repeatedQueriesKeys = true;
			}
            searchObject[split[0]] = split[1];
        }
		
		var ordered = {};
		Object.keys(searchObject).sort().forEach(function(key) {
			ordered[key] = searchObject[key];
			});
		
		if(repeatedQueriesKeys) {
			queryString = parser.search.replace(/^\?/, '');
		} else {
			queryString = JSON.stringify(ordered);
		}
		
        return {
            protocol: parser.protocol,
            host: parser.host,
            hostname: parser.hostname,
            port: parser.port || '80',
            pathname: parser.pathname,
            search: parser.search,
			username : parser.username ,
			password : parser.password ,
            searchObject: searchObject,
			queryString: queryString,
            hash: parser.hash
        };
    }

	
	function isSameURLs(url1,url2) {
		
		var url1Parsed = parseURL(url1);
		var url2Parsed = parseURL(url2);
		
		if( url1Parsed.protocol       == url2Parsed.protocol 
&& url1Parsed.hostname    == url2Parsed.hostname
&& url1Parsed.port        == url2Parsed.port
&& url1Parsed.pathname    == url2Parsed.pathname
&& url1Parsed.username    == url2Parsed.username 
&& url1Parsed.password    == url2Parsed.password 
&& url1Parsed.queryString == url2Parsed.queryString
&& url1Parsed.hash        == url2Parsed.hash  ) {
			return true;
			} else {
				return false;
				}
	}
	

 var url1 = parseURL('http://uname:pwd@ABC.com:81/%7Esmith/further/../down/./home.html?a=1&b=2#hash1');
 var url2 = parseURL('http://uname:pwd@ABC.com:81/%7Esmith/further/../down/./home.html?b=2&a=1#hash1');
 
 console.log(isSameURLs(url1,url2));
 
 
 