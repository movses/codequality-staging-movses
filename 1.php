<?php

namespace controllers\public_api\rest\autofix\v1;

class listAutofix implements \controllers\controllerInterface
{

	public function __construct(
		private \App\repositories\autofix\AutofixHistory $autofixHistoryRepo,
		private \App\services\autofix\autofixHistoryFormatter $formatter,
		private \App\services\public_api\paginationParams $paginationParamsService,
	) {}

	public function handleRequest($request, $args, $response)
	{
		\Core\database\Servers::setLagTolerance("lax");

		$get_vars = $request->getQueryParams();
		[ 'page' => $page, 'per_page' => $per_page ] = $this->paginationParamsService->assertAndParseFromQueryParams($get_vars, max_per_page: 20);

		$raw_tasks = $this->autofixHistoryRepo->listTasks(
			date_from: 0,
			date_to: time(),
			status: 'all',
			type: 'all',
			repo_id: -1,
			page: $page,
			per_page: $per_page,
		);


		$formatted_tasks = $this->formatter->formatRows($raw_tasks, return_schema_type: 'public_api');

		$has_next_page = count($raw_tasks) == $per_page;
        $has_next_page_str = $has_next_page ? 'true' : 'false';
        header("X-Has-Next-Page: $has_next_page_str");

		return $formatted_tasks;
	}
}
