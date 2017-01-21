export default function routes($stateProvider, $urlRouterProvider, $locationProvider) {
  'ngInject';
	//$locationProvider.html5Mode({ enabled: true , requireBase: false });
	$urlRouterProvider.otherwise('/index');
	
	$stateProvider
	.state('index', {
    url: '/index',
    template: '<div ui-view></div> <kanban></kanban>'
  });
  
  
		
	
}
